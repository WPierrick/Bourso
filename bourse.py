#!/usr/bin/python
# -*- coding:utf-8 -*-
'''
"""Premier exemple avec Tkinter.

On crée une fenêtre simple qui souhaite la bienvenue à l'utilisateur.

"""

# On importe Tkinter
from tkinter import *

# On crée une fenêtre, racine de notre interface
fenetre = Tk()

# On crée un label (ligne de texte) souhaitant la bienvenue
# Note : le premier paramètre passé au constructeur de Label est notre
# interface racine
champ_label = Label(fenetre, text="Salut les Zér0s !")

# On affiche le label dans la fenêtre
champ_label.pack()

# On démarre la boucle Tkinter qui s'interompt quand on ferme la fenêtre
fenetre.mainloop()
>>> champ_label["text"]
'Salut les Zér0s !'
>>> champ_label["text"] = "Maintenant, au revoir !"
>>> champ_label["text"]
'Maintenant, au revoir !'
>>>
'''
'''

from tkinter import *


fenetre = Tk()

label = Label(fenetre, text ="Hello World")

label.pack()

fenetre.mainloop()
'''


class action:
	def __init__(self, nombreactions, cours, rendement):
		self.cours = cours
		self.nombreactions = nombreactions
		self.rendement = rendement

	def dividendes(self):
		newtot = self.rendement * self.nombreactions + self.nombreactions
		return newtot


	def argenttotal(self):
		toteur = self.nombreactions * self.cours
		return toteur



safran=action(input("Nombre d'actions"), input("cours"), input("dividendes"))
safran.dividendes()
safran.argenttotal()


print ("Capital détenu")
print (safran.argenttotal())

print ("Dividendes obtenus apres une annee")
print (safran.dividendes())
