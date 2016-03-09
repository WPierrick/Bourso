#!/usr/bin/python
# -*- coding:utf-8 -*-


class action:
	def __init__(self, nombreactions, cours, rendement):
		self.cours = cours
		self.nombreactions = nombreactions
		self.rendement = rendement

	def dividendes(self):
		newtot = self.rendement * self.nombreactions + self.nombreactions
		print (newtot)
		return newtot


	def argenttotal(self):
		toteur = self.nombreactions * self.cours
		#print (toteur)
		return toteur

safran=action(10, 50, 0.013,)
safran.dividendes()
safran.argenttotal()


print ("Capital détenu")
print (safran.argenttotal)

print ("Dividendes obtenus apres une annee")
print (safran.dividendes)