# -*- coding: utf-8 -*-
"""
Created on Wed Nov 15 18:11:08 2017

Exercices avec COUNT, MIN, MAX

@author: mdarq
"""

import sqlite3

connexion = sqlite3.connect('factbook.db')

query = "SELECT COUNT(birth_rate) FROM facts"
birth_rate_tuple = connexion.execute(query).fetchall()
print("Il y a {0} naissances non nulles".format(birth_rate_tuple[0][0]))

query = "SELECT MAX(birth_rate) FROM facts"
max_birth = connexion.execute(query).fetchall()
print("Le plus fort taux de naissance est: {0}".format(max_birth[0][0]))

#Afficher la plus petite croissance de population
query = "SELECT MIN(population_growth) FROM facts WHERE (population_growth!=0)"
min_growth = connexion.execute(query).fetchall()
print("Le plus petit taux de croissance de population est: {0} ".format(min_growth[0][0]))

#Afficher le plus fort taux de décès
query = "SELECT MAX(death_rate) FROM facts"
max_death = connexion.execute(query).fetchall()
print("Le plus fort taux de décès est: {0}".format(max_death[0][0]))