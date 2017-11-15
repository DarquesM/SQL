# -*- coding: utf-8 -*-
"""
Created on Sun Nov 12 21:33:39 2017

@author: mdarq
"""

import sqlite3
#%%

#Connect to database
connexion = sqlite3.connect('jobs.db')
#Create cursor
cursor = connexion.cursor()
#Sample query
query= "select * from recent_grads;"
#Execute query using cursor
cursor.execute(query)
#Fetch results
results = cursor.fetchall()
#Print first 2 results
print(results[:2])

#%%
'''
EXERCISE : écrire une requète qui retourne toutes les valeurs de la colonne Major
depuis la table recent_grads, stocker les résultats dans un tuple et assigner à majors
'''
query = "SELECT Major FROM recent_grads;"

cursor.execute(query)
majors = cursor.fetchmany(5)
#Other solution
major = cursor.execute(query).fetchmany(5)
print(majors)

#Close connection

connexion.close()
#%%

'''
EXERCISE : connect to database jobs.db, get majors and return in inverse alphabetical order
close connexion to database
'''

connexion = sqlite3.connect('jobs.db')
cursor = connexion.cursor()

query = "SELECT Major from recent_grads ORDER BY Major desc"
result = cursor.execute(query).fetchall()
print(result)
connexion.close()