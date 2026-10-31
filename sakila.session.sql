SELECT category.name AS category ,COUNT(*) AS num_films, AVG(length) AS avg_length
FROM film, film_category,category
WHERE film.film_id = film_category.film_id
AND category.category_id = film_category.category_id
GROUP BY category.category_id
HAVING COUNT(*) >= 60
AND AVG(length) > 110
ORDER BY avg_length DESC
