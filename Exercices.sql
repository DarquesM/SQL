-- Exercice : afficher les 5 premières catégories dont la majeur est arts
select Major, Major_category
from recent_grads
where Major_category like "arts"
limit 5 ;

-- Exercice : Retourner toutes les majors différentes de engineering
-- Avec un salaire médian <= 50000
-- OU avec un taux de personnes sans emploi > 6.5%

select Major, Total, Median, Unemployment_rate, Major_category
from recent_grads
where (
	(Median <= 50000) OR (Unemployment_rate > 0.065))
	AND (Major_category != "Engineering")
;