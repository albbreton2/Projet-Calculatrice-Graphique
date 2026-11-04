import customtkinter as ctk
import tkinter as tk
import numpy as np
from accueil import Accueil
from calculatrice import Calculatrice


class MainApp(ctk.CTk):
    def __init__(self):
        super().__init__()
        self.title("Calculatrice graphique")
        self.geometry("1280x800")
        self.grid_columnconfigure(0, weight=1)
        self.grid_rowconfigure(0, weight=1)

        self.axe1 = np.linspace(-10, 10, 100)
        self.axe2 = self.axe1 ** 2

        self.page = None
        self.create_menu()
        self.show_calculatrice()
        self.protocol("WM_DELETE_WINDOW", self.on_closing)   # idée de ta camarade

    def _afficher(self, page):
        if self.page is not None:
            self.page.destroy()
        self.page = page
        self.page.grid(row=0, column=0, sticky="nsew")

    def show_accueil(self):
        self._afficher(Accueil(self, axe1=self.axe1, axe2=self.axe2))

    def show_calculatrice(self):
        self._afficher(Calculatrice(self))

    def create_menu(self):
        menu_bar = tk.Menu(self)
        self.config(menu=menu_bar)
        file_menu = tk.Menu(menu_bar, tearoff=0)
        menu_bar.add_cascade(label="Fichier", menu=file_menu)
        file_menu.add_command(label="Quitter", command=self.on_closing)
        view_menu = tk.Menu(menu_bar, tearoff=0)
        menu_bar.add_cascade(label="Affichage", menu=view_menu)
        view_menu.add_command(label="Calculatrice", command=self.show_calculatrice)
        view_menu.add_command(label="Accueil (exercice)", command=self.show_accueil)

    def on_closing(self):
        self.quit()
        self.destroy()


if __name__ == "__main__":
    app = MainApp()
    app.mainloop()