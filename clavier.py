import customtkinter as ctk
import tkinter as tk
import numpy as np
import matplotlib.pyplot as plt

#class Clavier():
    #def __init__(self, master=None):
    #super().__init__(master)
    #self.master = master
    #self.create_widgets()

    #def create_widgets(self):

#quand on clique sur la touche, ça print la touche (changera le label/entry éventuellement)
def buttonClick(symbole):
    print(symbole)

#temporaire
clavier = ctk.CTk()
clavier.geometry('1280x300')
clavier.grid_columnconfigure(0,weight=1)

#Frame temporaire
clavierFrame = ctk.CTkFrame(clavier, height=300, width=400)
clavierFrame.grid(row=0, column=0, pady=(30,20))

#bouton x
xButton = ctk.CTkButton(clavierFrame, text="x", command=lambda: buttonClick("x"), height=20, width=80)
xButton.grid(row=0, column=0, pady=(5,5), padx=(5,5))

#bouton y
yButton = ctk.CTkButton(clavierFrame, text="y", command=lambda: buttonClick("y"), height=20, width=80)
yButton.grid(row=0, column=1, pady=(5,5), padx=(5,5))

#bouton pi
piButton = ctk.CTkButton(clavierFrame, text="π", command=lambda: buttonClick("π"), height=20, width=80)
piButton.grid(row=0, column=2, pady=(5,5), padx=(5,5))

#bouton e
eButton = ctk.CTkButton(clavierFrame, text="e", command=lambda: buttonClick("e"), height=20, width=80)
eButton.grid(row=0, column=3, pady=(5,5), padx=(5,5))

clavier.mainloop()