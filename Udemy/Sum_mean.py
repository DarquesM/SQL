# -*- coding: utf-8 -*-
"""
Created on Thu Nov 16 10:39:13 2017

@author: mdarq
"""

import sqlite3

#%%
#Create a connexion instance
connexion = sqlite3.connect('factbook.db')
#create a cursor
cursor = connexion.cursor()

#queries
query = "SELECT SUM(population) FROM facts;"
query2 = "SELECT AVG(population_growth) FROM facts WHERE population_growth!=0 AND area_land!=0;"

#fetchall returns tuples, so do not forget to get [0][0]
total_pop = cursor.execute(query).fetchall()[0][0]
mean_growth = cursor.execute(query2).fetchall()[0][0]

print("Total population: {0}\n Mean growth rate: {1}".format(total_pop, mean_growth))

#Combine functions
query3 = "SELECT SUM(population), AVG(population), MAX(birth_rate) FROM facts;"

total_pop, avg_pop, max_birth = cursor.execute(query3).fetchall()[0]
