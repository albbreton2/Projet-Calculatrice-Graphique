import customtkinter as ctk
from clavier import Clavier
from graphique import Graphique


#création de fonction par rapport à une touche du clavier

class Fonctions2d:
    def __init__(self,master):
        super().__init__(master)
        self.entree = ctk.CTkEntry(self, width=300)
        self.entree.grid(row=0, column=0, padx=10, pady=10)
    self.clavier = Clavier(self, on_key=self.inserer)
    self.clavier.grid(row=1, column=0)

    def inserer(self, texte):
        self.entree.insert("insert", texte)

    ctk.CTKButton(self, text="Tracer", command=self.tracer).grid(row=0, column=1, padx=5)

    def Tracer(self):
        texte = self.entree.get()
        print("Tracer :", texte)