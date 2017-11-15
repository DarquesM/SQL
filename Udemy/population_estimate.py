import pandas as pd 
import sqlite3
import math 

connexion = sqlite3.connect('factbook.db')

#Using pandas to read SQL table as pandas DataFrame
a = pd.read_sql_query("SELECT * FROM facts;", con = connexion)

print(a)

'''
Estimate population as of 2050 for each country, provided the pop growth is constant until then
N = N0*e**(rt)
N = final pop
N0 = initial pop
r = growth rate
t = number of years
'''

def popgrowth(df):
    return df["population"]*math.e**(df["population_growth"]*35/100)
    
#Create a new colum in the dataframe that will contain the estimated population as of 2050
a["pop_2050"] = popgrowth(a)

#Remove NaN
a = a.dropna(axis=0)

#Ignore countries with area or population = 0
a = a[(a['population']>0) & (a['area_land']>0)]

#Now return the name of the 10 most populated countries in 2050

most_pop_countries = list((a.sort_values(by=['pop_2050'],ascending=False))['name'].head(10))
print(most_pop_countries)

#Other way
#(a.sort_values(by=['pop_2050'],ascending=False))['name'].iloc[:10]
