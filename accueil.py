import customtkinter as ctk
import tkinter as tk
import matplotlib.pyplot as plt
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg



class Accueil(ctk.CTkFrame):
    def __init__(self, master=None):
        super().__init__(master)
        self.master = master
        self.axe1 = axe1
        self.axe2 = axe2
        self.create_widgets()
        self.master.protocol("WM_DELETE_WINDOW",self.quit)

    def create_widgets(self):
        
        self.grid(row=0, column=0, padx=20, pady=20, sticky="nsew") # Grille
    
        self.button = ctk.CTkButton(self, text="my button", command=self.button_callback)  # Bouton
        self.button.grid(row=0, column=0, pady=(20,10))
    
        self.label = ctk.CTkLabel(self, text="CTkLabel", fg_color="transparent")# Label
        self.label.grid(row=1, column=0, pady=(10,10))
        plt.figure(figsize = (5,4))
        plt.plot(self.axe1, self.axe2, label ='L'axe 1', color 'r')
        plt.title('Graphique')
        plt.xlabel('abscices')
        plt.ylabel('ordonnés')            
        plt.legend()
        plt.grid()

    

    def button_callback(self):
        print("button clicked")
        self.label.configure(text="Vous avez cliqué sur le bouton")
    