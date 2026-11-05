import customtkinter as ctk
import tkinter as tk
from graphique import Graphique
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
        ctk.CTkButton(haut, text= "☰", width = 40, command = self.ouvrir_menu).pack(side = "left", padx =5, pady = 5)
        ctk.CTkLabel(haut, text="Calculatrice graphique", font=("Arial", 22)).pack(side="left", padx=10)
        verticale = ctk.CTkFrame(self, width = 50)
        verticale.grid(row =1, column =0, sticky= "ns")
        ctk.CTkButton(verticale, text="+", width=40, command = self.ajouter_ligne).pack(padx=5, pady=5)
        self.bouton_geo = ctk.CTkButton(verticale, text="△", width=40, command = self.mode_geometrie)
        self.bouton_geo.pack(padx=5, pady=5)
        self.couleur_bouton = self.bouton_geo.cget("fg_color")
        ctk.CTkButton(verticale, text="✖", width=40, command = self.effacer_geometrie).pack(padx=5, pady=5)

        panneau = ctk.CTkFrame(self, width = 300)
        panneau.grid(row=1, column=1, sticky="ns")
        self.liste = ctk.CTkScrollableFrame(panneau, width=280)
        self.liste.pack(fill="both", expand=True)

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
        entree.pack(fill="x", padx=5, pady=3)
        entree.bind("<FocusIn>", lambda e, en=entree: setattr(self, "entree_active", en))
        self.lignes.append(entree)
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
