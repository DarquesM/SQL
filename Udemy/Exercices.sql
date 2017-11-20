-- Exercice : afficher les 5 premières catégories dont la majeur est arts
select Major, Major_category
from recent_grads
where Major_category like "arts"
limit 5 ;

/* Exercice : Retourner toutes les majors différentes de engineering
Avec un salaire médian <= 50000
OU avec un taux de personnes sans emploi > 6.5% */

select Major, Total, Median, Unemployment_rate, Major_category
from recent_grads
where (
	(Median <= 50000) OR (Unemployment_rate > 0.065))
	AND (Major_category != "Engineering")
;

/* Exercice : Retourner les 20 premieres majors dont la catégorie est différente de engineering
Trier les résultats dans l'ordre alphabétique
*/ 

select Major
from recent_grads
where Major_category not like "Engineering"
order by Major 
limit 20
;

/*
Exercice : Sommer la population de tous les pays pour trouver la population totale
*/

select sum(population)
from facts
where name not like 'world' and area_land !='';


#Count number of lines in the whole database
select count(*)
from facts;

#Count number of non null values
select count(population)
from facts;

#Combine operations
select sum(area_land), avg(area_water), COUNT(*)
from facts
;

/* Ecrire une requete qui donne la moyenne de la colonne population_growth
pour les pays ayant une population supérieur à 10 000 000 habitants
*/

SELECT AVG (population_growth)
FROM facts
WHERE population > 10000000
;

/*
Compter le nombre de valeurs uniques de birth_rate, on utilise COUNT pour ne pas tenir compte de la valeur NULL
*/

SELECT COUNT(birth_rate) /*241 lignes*/
FROM facts
;

SELECT DISTINCT birth_rate /*217, attention une valeur NULL */
FROM facts;

SELECT COUNT(DISTINCT birth_rate) /*216*/
FROM facts
;

/* Trouver la moyenne des valeurs disctinctes de birth_rate
pour une pop > 20 000 000
Trouver la somme de toutes les valeurs disctinctes de la population 
pour laquelle area_land est > 1 000 000*/

SELECT AVG(DISTINCT birth_rate)
FROM facts
WHERE population>20000000;

SELECT SUM(DISTINCT population)
FROM facts
WHERE area_land>1000000;

/*
Calculer le ration naissance/morts pour évaluer la croissance de la population
*/
SELECT (birth_rate+migration_rate)/death_rate, name, population_growth
FROM facts 
WHERE death_rate!=0 AND birth_rate!=0
;

/*Ecrire une requête pour calculer le nombre d'habitants au 1er janvier 2016 pour chaque pays*/
query = "SELECT (population*population_growth)+population FROM facts;"

