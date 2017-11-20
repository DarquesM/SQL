# -*- coding: utf-8 -*-
"""
Created on Thu Nov 16 13:12:40 2017

@author: mdarq
"""

import sqlite3

connexion = sqlite3.connect('factbook.db')
cursor = connexion.cursor()

#Estimate the population growth rate from birth, immigration and death_rate
query = "SELECT (birth_rate+migration_rate)/death_rate FROM facts WHERE death_rate!=0 and birth_rate!=0;"
ratio = cursor.execute(query).fetchall()

#Ecrire une requête pour calculer le nombre d'habitants au 1er janvier 2016 pour chaque pays
query = "SELECT (population*population_growth)+population FROM facts;"

pop_2016 = cursor.execute(query).fetchall()