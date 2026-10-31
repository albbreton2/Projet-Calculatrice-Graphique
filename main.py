import customtkinter as ctk
import tkinter as tk
import numpy as np
import matplotlib.pyplot as plt
from clavier import Clavier

class MainApp(ctk.CTk):
    def __init__(self):
        super().__init__()
        self.geometry('1280x800')
        self.grid_columnconfigure(0, weight=1)

        ####### entry temporaire pour tester #######
        self.entry = ctk.CTkEntry(self)
        self.entry.grid(row=0,column=0,rowspan=100,sticky="new")
        ############################################

        self.afficheClavier()

    def afficheClavier(self):        
        clavier = Clavier(master=self)
        clavier.grid(row=900, column=0, sticky="sew")


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


if __name__ == "__main__":
    app = MainApp()
    app.mainloop()