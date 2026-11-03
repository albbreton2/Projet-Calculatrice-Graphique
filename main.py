import customtkinter as ctk
import tkinter as tk
import numpy as np
import matplotlib.pyplot as plt
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg, NavigationToolbar2Tk
from matplotlib.figure import Figure
from clavier import Clavier

class MainApp(ctk.CTk):
    def __init__(self):
        super().__init__()
        self.geometry('1280x700')
        self.grid_rowconfigure(0, weight=1)
        self.grid_columnconfigure(0, weight=1)

        ####### entry temporaire pour tester #######
        frameEntry1 = ctk.CTkEntry(self, width=400)
        frameEntry1.grid(row=0,column=0,sticky="nw")
        self.entry = ctk.CTkEntry(frameEntry1)
        self.entry.grid(row=0,column=0,sticky="new")
        ############################################

        ##### graphique #####################################
        fig = Figure(figsize=(11,8))
        ax = fig.add_subplot(111)
        x=np.linspace(-10, 10, 500)
        y=x**2
        ax.plot(x,y)

        # Intégrer le graphique dans tkinter
        graphFrame = ctk.CTkFrame(self)
        graphFrame.grid(row=0, column=1, sticky="nw")
        graphFrame.grid_columnconfigure(0, weight=1)
        graphFrame.grid_rowconfigure(0, weight=1)
        #window.canvas = FigureCanvasTkAgg(plt.gcf(), master=graphFrame)
        canvas = FigureCanvasTkAgg(fig, master=graphFrame)
        canvas.draw()
        canvas.get_tk_widget().grid(row=0, column=0)

        toolbarFrame = ctk.CTkFrame(master=self)
        toolbarFrame.grid(row=1,column=1)
        toolbar = NavigationToolbar2Tk(canvas, toolbarFrame, pack_toolbar=False)
        toolbar.update()
        toolbar.grid(row=0, column=0)

        self.protocol("WM_DELETE_WINDOW", self.on_closing)
        ############################################

        self.afficheClavier()

    def afficheClavier(self):        
        clavier = Clavier(master=self)
        clavier.grid(row=2, column=0, columnspan=2, sticky="sew")


    def changeEntry(self, symbole):
        current = str(self.entry.get()) #prend ce qu'il y a déjà dans l'entry
        pos = self.entry.index("insert") #prend la position courante du curseur
        self.entry.delete(0, tk.END) #supprime l'entièreté des caractères de l'entry

        entryText = ""
        if current == "": #si c'est le premier caractère ajouté
            entryText += str(symbole)
        elif pos == len(current): #si c'est le dernier caractère
            entryText = current + str(symbole)
        else:
            for i in range (len(current)): #pour toutes les lettres de current,
                if i == pos: #si la position de la lettre est la position du symbole à ajouter
                    entryText += str(symbole) #ajoute le symbole à la chaine de caractères
                    entryText += current[i]
                else: #sinon
                    entryText += current[i] #ajoute le reste de la chaine de caractères
        self.entry.insert(0, entryText)

    def backspaceEntry(self):
        current = str(self.entry.get()) #prend ce qu'il y a déjà dans l'entry
        pos = self.entry.index("insert") #prend la position courante du curseur
        self.entry.delete(0, tk.END) #supprime l'entièreté des caractères de l'entry

        entryText = ""
        for i in range (len(current)): #pour toutes les lettres de current,
            if i != pos-1: #si la position de la lettre n'est la position de la lettre à effacer
                entryText += current[i] #ajouter la lettre à la chaine de caractères
        self.entry.insert(0, entryText) #insère le texte dans l'entry

    def on_closing(self):
        self.quit()
        self.destroy()


if __name__ == "__main__":
    app = MainApp()
    app.mainloop()