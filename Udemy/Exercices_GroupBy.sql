/*
Using database jobs.db
*/

--Somme des étudiants ayant trouvé un emploi par catégorie
SELECT SUM(employed),Major_category
FROM recent_grads
GROUP BY Major_category;

--Pourcentage moyen de femmes pour chaque catégorie de majors
SELECT Major_category,AVG(ShareWomen)*100 AS Women_Share
FROM recent_grads
GROUP BY Major_category;

--Exemple de renommage de colonnes
SELECT SUM(Men) as total_men, SUM(women) as total_women
FROM recent_grads
;