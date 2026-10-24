import customtkinter as ctk
import tkinter as tk
import numpy as np
import matplotlib.pyplot as plt
from MathConstante import MathConstante
from MathConstante import MathFonction


class Clavier(ctk.CTkFrame):
    def __init__(self, master=None):
        super().__init__(master)
        self.master = master
        self.create_widgets()

    def create_widgets(self):

        ##################################################################################################################
        ## La section ici est la première section du clavier, commentée pour l'instant car il y aura plusieurs claviers ##
        ##################################################################################################################
        '''
        #bouton x
        xButton = ctk.CTkButton(self, text="x", command=lambda: buttonClick("x"), height=20, width=80)
        xButton.grid(row=0, column=0, pady=(5,5), padx=(5,5))

        #bouton y
        yButton = ctk.CTkButton(self, text="y", command=lambda: buttonClick("y"), height=20, width=80)
        yButton.grid(row=0, column=1, pady=(5,5), padx=(5,5))

        #bouton pi
        pi = MathConstante("pi")
        piButton = ctk.CTkButton(self, text=pi.__str__(), command=lambda: buttonClick(pi), height=20, width=80)
        piButton.grid(row=0, column=2, pady=(5,5), padx=(5,5))

        #bouton e
        e = MathConstante("e")
        eButton = ctk.CTkButton(self, text="e", command=lambda: buttonClick(e), height=20, width=80)
        eButton.grid(row=0, column=3, pady=(5,5), padx=(5,10))

        #bouton a²
        squareButton = ctk.CTkButton(self, text="a²", command=lambda: buttonClick("²"), height=20, width=80)
        squareButton.grid(row=1, column=0, pady=(5,5), padx=(5,5))

        #bouton exposant
        exposantButton = ctk.CTkButton(self, text="a^x", command=lambda: buttonClick("^x"), height=20, width=80)
        exposantButton.grid(row=1, column=1, pady=(5,5), padx=(5,5))

        #bouton sqrt
        sqrt = MathFonction("sqrt")
        sqrtButton = ctk.CTkButton(self, text=sqrt.__str__(), command=lambda: buttonClick(sqrt), height=20, width=80)
        sqrtButton.grid(row=1, column=2, pady=(5,5), padx=(5,5))

        #bouton valeur absolue
        absolute = MathFonction("absolute")
        absoluteButton = ctk.CTkButton(self, text=absolute.__str__(), command=lambda: buttonClick(absolute), height=20, width=80)
        absoluteButton.grid(row=1, column=3, pady=(5,5), padx=(5,10))

        ppButton = ctk.CTkButton(self, text="<", command=lambda: buttonClick("<"), height=20, width=80)
        ppButton.grid(row=2, column=0, pady=(5,5), padx=(5,5))

        pgButton = ctk.CTkButton(self, text=">", command=lambda: buttonClick(">"), height=20, width=80)
        pgButton.grid(row=2, column=1, pady=(5,5), padx=(5,5))

        sevenButton = ctk.CTkButton(self, text="7", command=lambda: buttonClick(7), height=20, width=80)
        sevenButton.grid(row=0, column=4, pady=(5,5), padx=(10,5))

        eightButton = ctk.CTkButton(self, text="8", command=lambda: buttonClick(8), height=20, width=80)
        eightButton.grid(row=0, column=5, pady=(5,5), padx=(5,5))

        nineButton = ctk.CTkButton(self, text="9", command=lambda: buttonClick(9), height=20, width=80)
        nineButton.grid(row=0, column=6, pady=(5,5), padx=(5,5))

        fourButton = ctk.CTkButton(self, text="4", command=lambda: buttonClick(4), height=20, width=80)
        fourButton.grid(row=1, column=4, pady=(5,5), padx=(10,5))

        fiveButton = ctk.CTkButton(self, text="5", command=lambda: buttonClick(5), height=20, width=80)
        fiveButton.grid(row=1, column=5, pady=(5,5), padx=(5,5))

        sixButton = ctk.CTkButton(self, text="6", command=lambda: buttonClick(6), height=20, width=80)
        sixButton.grid(row=1, column=6, pady=(5,5), padx=(5,5))

        oneButton = ctk.CTkButton(self, text="1", command=lambda: buttonClick(1), height=20, width=80)
        oneButton.grid(row=2, column=4, pady=(5,5), padx=(10,5))

        twoButton = ctk.CTkButton(self, text="2", command=lambda: buttonClick(2), height=20, width=80)
        twoButton.grid(row=2, column=5, pady=(5,5), padx=(5,5))

        threeButton = ctk.CTkButton(self, text="3", command=lambda: buttonClick(3), height=20, width=80)
        threeButton.grid(row=2, column=6, pady=(5,5), padx=(5,5))

        zeroButton = ctk.CTkButton(self, text="0", command=lambda: buttonClick(0), height=20, width=80)
        zeroButton.grid(row=3, column=4, pady=(5,5), padx=(10,5))
        '''

        ####################################
        ## section des lettres du clavier ##
        ####################################

        letters= ['q','w','e','r','t','y','u','i','o','p',
                  'a','s','d','f','g','h','j','k','l',
                  ' ↑ ','z','x','c','v','b','n','m'] #liste des lettres du clavier
        lettersButtons = [] #liste des boutons du clavier

        for letter in letters:
            lettersButtons.append(ctk.CTkButton(self, text=letter, command=lambda btn=letter: buttonClick(btn), height=20, width=60))
        lettersButtons.append(ctk.CTkButton(self, text='⌫', command=lambda: backspaceButton(), height=20, width=60))

        col, row = 0, 0 #compteurs
        for i in range(len(lettersButtons)):
            if col == 10 and row == 0:  #pour que ce soit placé selon la bonne ligne et colonne
                col, row = 0, 1
            if col == 9 and row == 1:
                col, row = 0, 2
            lettersButtons[i].grid(row=row, column=col, pady=(5,5), padx=(5,5)) #
            col += 1
        lettersButtons[19].configure(command=lambda: capitalizeLetters(lettersButtons)) #Pour mettre en majuscule/minuscule

#quand on clique sur la touche, ça print la touche (changera le label/entry éventuellement)
def buttonClick(symbole):
    print(symbole)
    ################################
    ##Pour cliquer sur une touche:##
    ################################
    #current = entry.get()
    #entry.delete(0, tk.END)
    #entry.insert(0, str(current) + str(symbole))

#supprime le dernier caractère entré
def backspaceButton():
    print("*supprime dernier caractère*")
    ########################################
    ##Pour supprimer le dernier caractère:##
    ########################################
    #current = str(entry.get())
    #entry.delete(0, tk.END)
    #entry.insert(0, current[:len(current)-1])

#met en majuscules ou en minuscules
def capitalizeLetters(lettersBtn):
    for i in lettersBtn:
        if i.cget("text")!=" ↑ " and i.cget("text")!="⌫": #si ce n'est pas une touche qui n'est pas une lettre
            if i.cget("text").isupper(): #si l'attribut text du bouton est en majuscules
                lowerLetter = i.cget("text").lower() #mettre en minuscule
                i.configure(text = lowerLetter, command=lambda lettre=lowerLetter: buttonClick(lettre))
            else: #si l'attribut text du bouton est en minuscules
                upperLetter = i.cget("text").upper() #mettre en majuscules
                i.configure(text = upperLetter, command=lambda lettre=upperLetter: buttonClick(lettre))