'''
UTILISER PYTHON AVEC SQLITE
'''

import sqlite3
connexion = sqlite3.connect("factbook.db")

#Cursor
c = connexion.cursor()
#c.execute('SELECT * FROM facts;')

#print(c.fetchall())

'''
Modifier le code ci-dessus pour sélectionner les 10 pays les moins peuplés
Exécuter depuis la ligne de commande
'''

query = "SELECT name FROM facts ORDER BY population ASC LIMIT 10"
c.execute(query)
print(c.fetchall())