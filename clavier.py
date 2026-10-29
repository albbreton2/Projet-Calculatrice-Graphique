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

        ####################################
        ## section des lettres du clavier ##
        ####################################
        '''
        letters= ['q','w','e','r','t','y','u','i','o','p',
                  'a','s','d','f','g','h','j','k','l',
                  ' ▲ ','z','x','c','v','b','n','m'] #liste des lettres du clavier
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
        '''

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