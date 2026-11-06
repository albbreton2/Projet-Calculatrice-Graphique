import customtkinter as ctk
import matplotlib.pyplot as plt
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg


class Accueil(ctk.CTkFrame):
    def __init__(self, master=None, axe1=None, axe2=None):
        super().__init__(master)
        self.axe1 = axe1
        self.axe2 = axe2
        self.create_widgets()

    def create_widgets(self):
        self.button = ctk.CTkButton(self, text="my button", command=self.button_callback)
        self.button.grid(row=0, column=0, pady=(20, 10))

        self.label = ctk.CTkLabel(self, text="CTkLabel", fg_color="transparent")
        self.label.grid(row=1, column=0, pady=(10, 10))

        plt.figure(figsize=(5, 4))
        plt.plot(self.axe1, self.axe2, label="Le carré de l'axe 1", color="r")
        plt.title("Graphique")
        plt.xlabel("abscisses")
        plt.ylabel("ordonnées")
        plt.legend()
        plt.grid()

        self.canvas = FigureCanvasTkAgg(plt.gcf(), master=self)
        self.canvas.draw()
        self.canvas.get_tk_widget().grid(row=2, column=0, pady=(10, 10))

    def button_callback(self):
        print("button clicked")
        self.label.configure(text="Vous avez cliqué sur le bouton")
