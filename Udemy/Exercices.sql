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