import customtkinter as ctk
import tkinter as tk
import numpy as np
import matplotlib.pyplot as plt
from MathConstante import MathConstante
from MathConstante import MathFonction

class ClavierAccueil(ctk.CTkFrame):
    def __init__(self, master=None):
        super().__init__(master)
        self.master = master
        self.create_widgets()

    def create_widgets(self):
        listeOperateurs = ['x', 'y', MathConstante("pi"), MathConstante("e"),
                           '²', MathFonction("**"), MathFonction("sqrt"), MathFonction("absolute"),
                           '(', ')', '<', '>',
                           MathFonction("cbrt"), ',' ,'≤' ,'≥']
        listeBoutons1 = []

        for symbole in listeOperateurs:
            if type(symbole) == '__main__.MathFonction' or type(symbole) == '__main__.MathConstante':
                listeBoutons1.append(ctk.CTkButton(self, text=symbole.__str__(), command=lambda btn=symbole: buttonClick(btn), height=20, width=80))
            else:
                listeBoutons1.append(ctk.CTkButton(self, text=symbole, command=lambda btn=symbole: buttonClick(btn), height=20, width=80))

        count, padx3 = 0, 5
        for i in range(4):
            for j in range(0,4):
                if j == 4:
                    padx3 = 15
                else:
                    padx3 = 5
                if count<len(listeOperateurs):
                    listeBoutons1[count].grid(row=i, column=j, pady=(5,5), padx=(padx3,5))
                    count += 1
        
        chiffres = [7,8,9,'÷',4,5,6,'×',1,2,3,'-',0,'.','=','+']
        chiffresBoutons = []

        for chiffre in chiffres:
            chiffresBoutons.append(ctk.CTkButton(self, text=str(chiffre), command=lambda btn=chiffre: buttonClick(btn), height=20, width=80))

        count, padx4 = 0, 5
        for i in range(4):
            for j in range(4,8):
                if j == 4:
                    padx4 = 15
                else:
                    padx4 = 5
                if count<len(chiffres):
                    chiffresBoutons[count].grid(row=i, column=j, pady=(5,5), padx=(padx4,5))
                    count += 1

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