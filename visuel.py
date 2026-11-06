import customtkinter as ctk
import tkinter as tk
import numpy as np
from Graphique import Graphique
from clavier import Clavier


class Visuel(ctk.CTkFrame):
    def __init__(self,master):
        super().__init__(master)
        self.lignes = []
        self.entree_active = None

       
        self.mode_geo = False     
        self.points = []          
        self.selection = []       
        self.segments = []        

        self.grid_columnconfigure(2, weight=1)
        self.grid_rowconfigure(1, weight=1)

        haut = ctk.CTkFrame(self)
        haut.grid(row = 0, column =0, columnspan =3, sticky = "ew")
        ctk.CTkButton(haut, text= "☰", width = 40, command = self.ouvrir_menu).grid(row=0, column=0, padx=5, pady=5)
        ctk.CTkLabel(haut, text="Calculatrice graphique", font=("Arial", 22)).grid(row=0, column=1, padx=10, sticky="w")
        verticale = ctk.CTkFrame(self, width = 50)
        verticale.grid(row =1, column =0, sticky= "ns")
        ctk.CTkButton(verticale, text="+", width=40, command = self.ajouter_ligne).grid(row=0, column=0, padx=5, pady=5)
        self.bouton_geo = ctk.CTkButton(verticale, text="△", width=40, command = self.mode_geometrie)
        self.bouton_geo.grid(row=1, column=0, padx=5, pady=5)
        self.couleur_bouton = self.bouton_geo.cget("fg_color")
        ctk.CTkButton(verticale, text="✖", width=40, command = self.effacer_geometrie).grid(row=2, column=0, padx=5, pady=5)

        panneau = ctk.CTkFrame(self, width = 300)
        panneau.grid(row=1, column=1, sticky="ns")

        panneau.grid_rowconfigure(0, weight=1)
        panneau.grid_columnconfigure(0, weight=1)

        self.liste = ctk.CTkScrollableFrame(panneau, width=280)
        self.liste.grid(row=0, column=0, sticky="nsew")
        self.liste.grid_columnconfigure(0, weight=1)

        self.graphique = Graphique(self)
        self.graphique.grid(row=1, column=2, sticky="nsew")
        self.graphique.on_clic = self.clic_graphique

        # clavier tout en bas, sous les trois colonnes
        self.clavier = Clavier(self, on_key=self.inserer)
        self.clavier.grid(row=2, column=0, columnspan=3, pady=(5, 0))

        self.ajouter_ligne()

    def ouvrir_menu(self):
        menu = tk.Menu(self, tearoff=0)
        menu.add_command(label="Enregistrer", command=lambda: print("enregistrer"))
        menu.add_command(label="Documentation", command=lambda: print("doc"))
        menu.tk_popup(self.winfo_pointerx(), self.winfo_pointery())


    def ajouter_ligne(self):
        entree = ctk.CTkEntry(self.liste, placeholder_text="ex : sin(x)")
        entree.grid(row=len(self.lignes),column=0,sticky="ew",padx=5,pady=3)
        entree.bind("<FocusIn>", lambda e, en=entree: setattr(self, "entree_active", en))

        bouton = ctk.CTkButton(self.liste,text="+",width=30,command=lambda: self.dessiner_fonction(entree))
        bouton.grid(row=len(self.lignes),column=1,padx=(2, 5),pady=3)

        self.lignes.append((entree,bouton))
        self.entree_active = entree

    def inserer(self, texte):
        if self.entree_active is None:
            return
        if texte == "⌫":
            pos = self.entree_active.index("insert")
            if pos > 0:
                self.entree_active.delete(pos - 1)
        else:
            self.entree_active.insert("insert", texte)

    def dessiner_fonction(self, entree):
        x = np.linspace(-100,100,1000) #pour que ça ait l'air infini
        fonctionsPossibles={
            "÷": "/",
            "×": "*",
            "π": "np.pi",
            "∞": "np.inf",
            "√x": "np.sqrt(x)",
            "∛x": "np.cbrt(x)",
            "⌊x⌋": "np.floor(x)",
            "⌈x⌉": "np.ceil(x)",
            "eˣ": "np.exp(x)",
            "ln": "np.log",
            "log₁₀": "np.log10",
            "log₂": "np.log2",
            "|x|": "np.absolute(x)",
            "sin(x)": 'np.sin(x)',
            "cos(x)": 'np.cos(x)',
            "tan(x)": "np.tan(x)",
            "csc(x)": "(1/np.sin(x))",
            "sec(x)": "(1/np.cos(x))",
            "cot(x)": "(1/np.tan(x))",
            "arcsin(x)": "np.arcsin(x)",
            "arccos(x)": "np.arccos(x)",
            "arctan(x)": "np.arctan(x)",
            "arccsc(x)": "(1/np.arcsin(x))",
            "arcsec(x)": "(1/np.arccos(x))",
            "arccot(x)": "(1/np.arctan(x))",
            "²": '**2',
            "ˣ": "**(x)",
            "deg": "np.degrees",
            "rad": "np.radians",
            "≤": "<=",
            "≥": ">="
        }
        fonction = str(entree.get()) #prend l'entrée
        for i in fonctionsPossibles.keys():
            if i in fonction: #si c'est dans la fonction, remplacer par la version évaluable
                fonction = fonction.replace(i, fonctionsPossibles[i])
        
        peutEtreEvalue = False #Si la fonction peut-être évaluée, c'est vrai, sinon, c'est faux
        try:
            y = eval(fonction)
            peutEtreEvalue = True
        except Exception:
            peutEtreEvalue = False 
        if peutEtreEvalue: #S'affiche seulement si c'est évaluable, sinon rien ne s'affiche pour éviter une erreur
            self.graphique.tracer(x,y)


    def mode_geometrie(self):
        self.mode_geo = not self.mode_geo
        if self.mode_geo:
            self.bouton_geo.configure(fg_color="#2e7d32")   
        else:
            self.bouton_geo.configure(fg_color=self.couleur_bouton)
            self.selection = []
            self.redessiner_geometrie()

    def clic_graphique(self, x, y):
        if not self.mode_geo:
            return
        k = self.graphique.indice_point_proche(self.points, x, y)
        if k is None:                      
            self.points.append((x, y))
            k = len(self.points) - 1

        if k in self.selection:            
            self.selection.remove(k)
        else:
            self.selection.append(k)

        if len(self.selection) == 2:       
            i, j = self.selection
            if (i, j) not in self.segments and (j, i) not in self.segments:
                self.segments.append((i, j))
            self.selection = []
        self.redessiner_geometrie()

    def redessiner_geometrie(self):
        self.graphique.dessiner_geometrie(self.points, self.selection, self.segments)

    def effacer_geometrie(self):
        self.points = []
        self.selection = []
        self.segments = []
        self.redessiner_geometrie()
