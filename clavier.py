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

def yButtonClick():
    print("y")

app = ctk.CTk()
app.geometry('1280x800')
app.grid_columnconfigure(0,weight=1)

framee = ctk.CTkFrame(app, height=50, width=300)
framee.grid(row=0, column=0)
xButton = ctk.CTkButton(framee, text="x", command=yButtonClick height=20, width=80)
xButton.grid(row=0, column=0)
yButton = ctk.CTkButton(framee, text="y", height=20, width=80)
yButton.grid(row=0, column=1)
app.mainloop()