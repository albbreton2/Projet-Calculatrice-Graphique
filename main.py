import customtkinter as ctk
import tkinter as tk
import numpy as np
import matplotlib.pyplot as plt
from accueil import Accueil

#Création de la page graphique



class MainApp(ctk.CTk):
    def __init__(self):
        super().__init__()
        self.title("Calculatrice graphique")
        self.geometry("1200x800")
        self.show_accueil()
        self.axe1 = np.linspace(-10, 10, 100)
        self.axe2 = self.axe1 ** 2

    

    def show_accueil(self):
        self.accueil = Accueil(master=self, axe1 = self.axe1, axe2 = self.axe2)
    
    def create_menu(self):
        menu_bar = tk.Menu(self)
        self.config(menu=menu_bar)

        file_menu = tk.Menu(menu_bar, tearoff=0)
        menu_bar.add_cascade(label="Fichier", menu=file_menu)
        file_menu.add_command(label="Ouvrir", command=self.open_file)
        file_menu.add_command(label="Enregistrer", command=self.save_file)
        file_menu.add_separator()
        file_menu.add_command(label="Quitter", command=self.quit)
        edit_menu = tk.Menu(menu_bar, tearoff=0)
        menu_bar.add_cascade(label="Édition", menu=edit_menu)
        edit_menu.add_command(label="Annuler", command=self.undo_action)
        edit_menu.add_command(label="Rétablir", command=self.redo_action)
        view_menu = tk.Menu(menu_bar, tearoff=0)
        menu_bar.add_cascade(label="Affichage", menu=view_menu)
        view_menu.add_command(label="Accueil", command=self.show_accueil)
    
    def open_file(self):
        print("Ouvrir un fichier")
    def save_file(self):
        print("Enregistrer le fichier")
    def undo_action(self):
        print("Annuler")
    def redo_action(self):
        print("Rétablir")

    if __name__ == "__main__":
            app = MainApp()
            app.mainloop()
