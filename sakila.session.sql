SELECT COUNT(film_id) AS num_films , AVG(length) AS avg_length, MIN(replacement_cost) AS min_cost ,MAX(replacement_cost) AS max_cost
FROM film
WHERE description LIKE '%Documentary%'
AND special_features LIKE '%Commentaries%'
