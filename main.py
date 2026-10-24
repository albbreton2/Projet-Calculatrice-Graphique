import customtkinter as ctk
import tkinter as tk
import numpy as np
import matplotlib.pyplot as plt
from clavier import Clavier

class MainApp(ctk.CTk):
    def __init__(self):
        super().__init__()
        self.geometry('1280x800')
        self.afficheClavier()

    def afficheClavier(self):        
        clavier = Clavier(master=self)
        clavier.grid(row=900, column=0, sticky="s")

if __name__ == "__main__":
    app = MainApp()
    app.mainloop()