# -*- coding: utf-8 -*-
"""
Created on Wed Nov 15 17:00:58 2017

@author: mdarq

Exercice :
    Dans la table facts.db, calculer le ratio surface terrestre/surface ocean

"""

import sqlite3

#%%
connexion = sqlite3.connect('factbook.db')
cursor = connexion.cursor()

query = "SELECT SUM(area_land) FROM facts WHERE area_land!=''"
total_area_land = float(cursor.execute(query).fetchone()[0])

query = "SELECT SUM(area_water) FROM facts WHERE area_land!=''"
total_area_ocean = float(cursor.execute(query).fetchone()[0])

ratio = total_area_land/total_area_ocean

print("Ratio: {0}".format(ratio))