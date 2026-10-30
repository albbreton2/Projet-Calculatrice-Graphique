import customtkinter as ctk
import tkinter as tk
import numpy as np
import matplotlib.pyplot as plt
from MathConstante import MathConstante
from MathConstante import MathFonction
from clavierAccueil import ClavierAccueil
from clavierLettres import ClavierLettres


class Clavier(ctk.CTkFrame):
    def __init__(self, master=None):
        super().__init__(master)
        self.master = master
        self.grid_columnconfigure(1, weight=1)
        self.create_widgets()
        self.showClavierAccueil()

    def showClavierAccueil(self):
        self.clearClavierFrame()
        self.clavierAccueil = ClavierAccueil(self)
        self.clavierAccueil.grid(row=1, column=0, columnspan=20, sticky='s')

    def showClavierLettres(self):
        self.clearClavierFrame()
        self.clavierLettres = ClavierLettres(self)
        self.clavierLettres.grid(row=1, column=0, columnspan=30, sticky='s')
    '''
    def showClavierFonctions(self):
        self.clearClavierFrame()
        self.clavierFonctions = ClavierFonctions(self)
    
    def showClavierAutre(self):
        self.clearClavierFrame()
        self.clavierAutre = ClavierAutre(self)
    '''
    def clearClavierFrame(self):
        for widget in self.winfo_children():
            widget.destroy()
        self.create_widgets()
        


    def create_widgets(self):
        boutonAccueil = ctk.CTkButton(self, text="123", command = self.showClavierAccueil, height=20, width=40)
        boutonAccueil.grid(row=0, column=0, pady=(5,5), padx=(5,5), sticky="w")

        boutonLettres = ctk.CTkButton(self, text="ABC", command = self.showClavierLettres, height=20, width=40)
        boutonLettres.grid(row=0, column=1, pady=(5,5), padx=(5,5), sticky="w")

#quand on clique sur la touche, ça print la touche (changera le label/entry éventuellement)
def buttonClick(symbole):
    print(symbole)
    ################################
    ##Pour cliquer sur une touche:##
    ################################
    '''
    current = str(entry.get()) #prend ce qu'il y a déjà dans l'entry
    pos = entry.index(INSERT) #prend la position courante du curseur
    entry.delete(0, tk.END) #supprime l'entièreté des caractères de l'entry
    entryText = ""
    for i in range (len(current)): #pour toutes les lettres de current,
        if i == pos: #si la position de la lettre est la position du symbole à ajouter
            entryText += str(symbole) #ajoute le symbole à la chaine de caractères
        else: #sinon
            entryText += current[i] #ajoute le reste de la chaine de caractères
    entry.insert(0, entryText)
    '''

#supprime le dernier caractère entré
def backspaceButton():
    print("*supprime dernier caractère*")
    ########################################
    ##Pour supprimer le dernier caractère:##
    ########################################
    '''
    current = str(entry.get()) #prend ce qu'il y a déjà dans l'entry
    pos = entry.index(INSERT) #prend la position courante du curseur
    entry.delete(0, tk.END) #supprime l'entièreté des caractères de l'entry
    entryText = ""
    for i in range (len(current)): #pour toutes les lettres de current,
        if i != pos: #si la position de la lettre n'est la position de la lettre à effacer
            entryText += current[i] #ajouter la lettre à la chaine de caractères
    entry.insert(0, entryText) #insère le texte dans l'entry
    #entry.insert(0, current[:len(current)-1])
    '''

#met en majuscules ou en minuscules
def capitalizeLetters(lettersBtn):
    ###############################################
    ##Pour mettre en majuscules ou en minuscules:##
    ###############################################
    for i in lettersBtn:
        if i.cget("text").isalpha(): #si c'est une lettre
            if i.cget("text").isupper(): #si l'attribut text du bouton est en majuscules
                lowerLetter = i.cget("text").lower() #mettre en minuscule
                i.configure(text = lowerLetter, command=lambda lettre=lowerLetter: buttonClick(lettre))
            else: #si l'attribut text du bouton est en minuscules
                upperLetter = i.cget("text").upper() #mettre en majuscules
                i.configure(text = upperLetter, command=lambda lettre=upperLetter: buttonClick(lettre))