#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Dec  8 07:24:58 2020

@author: nathan
"""

"""
programme principal
"""

from fct import choimot, ouvrfichier
from classe import pendule

from tkinter import  PhotoImage



mot = choimot(ouvrfichier())    #mot aléatoire


fenetre=pendule(mot,200,500,250,250)  #initialise le pendule affiche la fenetre du pendule et initialise toute les varivales
fenetre.geometry("600x600") #defini la taille de la fenetre


#importe toute les images
image1=PhotoImage(file="bonhomme1.gif")
image2=PhotoImage(file="bonhomme2.gif")
image3=PhotoImage(file="bonhomme3.gif")
image4=PhotoImage(file="bonhomme4.gif")
image5=PhotoImage(file="bonhomme5.gif")
image6=PhotoImage(file="bonhomme6.gif")
image7=PhotoImage(file="bonhomme7.gif")
image8=PhotoImage(file="bonhomme8.gif")

#je renge dans une liste pour que se soit plus facil a utilise
L=[image8,image7,image6,image5,image4,image3,image2,image1]

#donne la liste des images a mon objet pendule
fenetre.setlesimges(L)

#affiche le canvas
fenetre.affichage()



fenetre.mainloop()
