import customtkinter as ctk
from graphique import Graphique


class Visuel:
    def __init__(self,master):
        super().__init__(master)
        self.entree = ctk.CTkEntry(self, width=300)
        self.entree.grid(row=0, column=0, padx=10, pady=10)
        self.graphique = Graphique(self)
        self.graphique.grid(row=0, column=2, rowspan=2, sticky="nsew")
        self.grid_columnconfigure(2, weight=1)
        self.grid_rowconfigure(1, weight=1)

        haut = ctk.CTkFrame(self)
        haut.grid(row = 0, column =0, columnspan =3, sticky = "ew")
        ctk.CTkButton(haut, text= "☰", width = 40, command = self.ouvrir_menu).pack(side = "left", padx =5, pady = 5)
        ctk.CTkLabel(haut, text="Calculatrice graphique", font=("Arial", 22)).pack(side="left", padx=10)
        
        verticale = ctk.CTkFrame(self, width = 50)
        verticale.grid(row =1, column =0, sticky= "ns")
        ctk.CTkButton(verticale, text="+", width=40, command = self.ajouter_ligne).pack(padx=5, pady=5)
        ctk.CTkButton(verticale, text="△", width=40, command = self.mode_geometrie).pack(padx=5, pady=5)
    


        self.graphique = Graphique(self)
        self.graphique.grid(row=1, column=2, sticky="nsew")

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
        print("mode points/segments")