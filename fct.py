#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Dec  1 08:14:47 2020

@author: nathan
"""
"""
Le fichier contient toute les fonctions du pendule
"""

from random import randint


"""
en entrée une liste de mot
choisi un mot dans liste de mot
return le mot choisi(str)
"""
def choimot(L):
    nb=randint(0,len(L)-1)
    return L[nb]



"""
ouvre le fichier mot.txt pour voir les mots qu'il y a
return la liste de mot dans le fichier mot.txt
"""
def ouvrfichier():
    fichier = open("mot.txt","r")
    txt = fichier.read()
    L = txt.split()
    fichier.close()
    return L


"""
en entrée (ce que le joueur a trouvé pour le mot(str),le nombre de faute, le mot a trouvé(str))
afficher le pendu + le lettre trouvé + si il a gagné
"""
def affich(mtrouver,faute,mot):
    L=["---------","| \n| \n---------","| \n| \n| \n| \n---------","|/ \n| \n| \n| \n| \n---------",
       "______ \n|/ \n| \n| \n| \n| \n---------","______ \n|/   | \n| \n| \n| \n| \n---------",
       "______ \n|/   | \n|    o \n|  \n| \n| \n---------",
       "______ \n|/   | \n|    o \n|   /|\ \n| \n| \n---------",
       "______ \n|/   | \n|    o \n|   /|\ \n|   / \ \n| \n---------"]
    print(L[faute])
    for  i in range(len(mtrouver)):
        print(mtrouver[i]+" ",end="")
        
    if mot == mtrouver:
        print("\nvous avez gagné")
    elif faute == 8:
        print("\nVous avez perdu")

    

"""
en entrée (le score maximum atteint, le nombre de faute du joueur)
affiche le score du joueur + le meilleur score
return le score maximum
"""    
def score(scoremax,faute):
    print("Votre score est de "+str(faute))
    if scoremax > faute:
        scoremax = faute
    print("Le meilleur score est de "+str(scoremax)+" faute")
    return scoremax
        
        

"""
en entrée (le mot a trouvé, le mot actuel du joueur, les lettres déjà utiliser, le nombre de faute)
vérifie si le joueur n'a pas redemander une lettre déjà demander
vérifie si le joueur a trouvé une bonne lettre
return le mot actuel du joueur, les lettres utilisé, le nombre de faute
"""
def verifmot(mot,mtrouver,mpasse,faute):
    mtrouver2=""
    u = 0
    lettre = str(input("Donner une lettre :"))
    while lettre in mpasse:
        lettre = str(input("Veuillez donner une lettre qui n'a jamais étais donné:"))
    mpasse.append(lettre)
    
    for i in range(len(mot)):
        if not mtrouver[i] == "_":
            mtrouver2 = mtrouver2 + mtrouver[i]
        elif lettre == mot[i] :
            mtrouver2=mtrouver2+lettre
            u+=1
        else:
            mtrouver2=mtrouver2+"_"
        
    if u == 0:
        faute+=1
    
    return mtrouver2, mpasse, faute 

