#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Dec  8 08:15:00 2020

@author: nathan
"""
"""
creation de la classe pendule
creation des fonciton pour la classe pendule
"""
from fct import choimot, ouvrfichier

from tkinter import Tk,Canvas, Entry, Button
from tkinter import messagebox


#creation d'une sous classe de tkinter
class pendule(Tk):
     
    #creation des variables
    def __init__(self,mot,xmot,ymot,ximage,yimage):
        Tk.__init__(self)  #affiche la fenetre
        self.__mot=mot      #le mot a trouver
        self.__mtrouver=self.inimtrouver()      #mot actuel du joueur  
        self.__faute=0      #le nombre d'erreur
        self.__mpasse=[]    #les lettres deja utiliser
        self.__lesimages=[]     #listes images pour afficher les pendules
        self.__xmot,self.__ymot=xmot,ymot      #coordonné du mot qui va etre afficher
        self.__ximage,self.__yimage=ximage,yimage     #coordonné de l'image afficher
        self.creer_widget()        #creation des widgets

        #fonction qui crée les widget de la fenetre
    def creer_widget(self):
            #crée un canvas et l'affiche en 0,0
            self.canvas=Canvas(self,width=1500, height=1000,background="white")
            self.canvas.place(x=0,y=0)
            
            #affiche toute les lettres trouver par le joueur
            self.canvas.create_text(self.__xmot,self.__ymot,text=self.__mtrouver)
            
            #crée l'entry lettre et l'affiche
            #permet a l'utilisateur de donner ça lettre
            self.Lettre = Entry(self, width=10)
            self.Lettre.place(x=475,y=450)

            #crée le bouton choisie et l'affiche
            #permet a l'utilisateur de vérifier si sa lettre est bonne
            self.Choisi = Button(self, text="Valider", command=self.verif)
            self.Choisi.place(x=475,y=475)
            
            #crée le bouton Re et l'affiche
            #permet a joueur de recommence la partie
            self.Re = Button(self,text="Recommencer", command=self.recommencer)
            self.Re.place(x=475,y=500)
  
      
        #initialise la variable __mtrouver
    def inimtrouver(self):
        mtrouver=self.__mot[0]
        for i in range(len(self.__mot)):
            mtrouver= mtrouver + "_"
        return mtrouver


        #donne les images du pendule a l'objet self
    def setlesimges(self,lesimages):
        for image in lesimages:
            self.__lesimages.append(image)


          #verifie si la lettre donner est bonne
    def verif(self):
        mtrouver2=""
        u = 0
        lettre = self.Lettre.get()
        if lettre in self.__mpasse:    #verifie si la lettre donner a était déja donner
            self.Lettre.delete(0,len(lettre))
            messagebox.showwarning("Erreur","Veuillez changer de lettre \n vous l'avez deja utiliser")
        elif len(lettre)!=1:      #verifie si on a bien UNE lettre
            self.Lettre.delete(0,len(lettre))
            messagebox.showwarning("Erreur","Veuillez mettre une lettre")
        else:
            self.__mpasse.append(lettre)
            self.Lettre.delete(0,len(lettre))
            for i in range(len(self.__mot)):
                if not self.__mtrouver[i] == "_":
                    mtrouver2 = mtrouver2 +self.__mtrouver[i]
                elif lettre == self.__mot[i] :
                    mtrouver2=mtrouver2+lettre
                    u+=1
                else:
                    mtrouver2=mtrouver2+"_"
            
            if u == 0:
                self.__faute+=1
            
            self.__mtrouver = mtrouver2
            self.affichage()
            
        #affiche le mot et le bonhomme 
    def affichage(self):
        self.canvas.delete("all")
        self.canvas.create_text(self.__xmot,self.__ymot,text=self.__mtrouver)
        self.canvas.create_image(self.__ximage, self.__yimage, image=self.__lesimages[self.__faute])
        if self.__faute == 7:
            messagebox.showwarning("Looser","Vous avez perdu")
        elif self.__mot == self.__mtrouver:
            messagebox.showinfo("Bien joué","Vous avez gagné")
            
        #initialise les variables de l'objet self pour recommencer une partie
    def recommencer(self):
        self.__faute = 0
        self.__mot=choimot(ouvrfichier())
        self.__mpasse=[]
        self.__mtrouver=self.inimtrouver()
        self.affichage()
         