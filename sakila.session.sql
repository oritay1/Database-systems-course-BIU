SELECT  CONCAT(a1.first_name, ' ', a1.last_name) AS actor1,
        CONCAT(a2.first_name, ' ', a2.last_name) AS actor2,
        COUNT(f1.actor_id) AS shared_films
FROM film_actor as f1, film_actor AS f2, actor AS a1, actor AS a2

WHERE f1.film_id = f2.film_id
AND f1.actor_id < f2.actor_id
AND f1.actor_id = a1.actor_id
AND f2.actor_id = a2.actor_id

GROUP BY f1.actor_id, f2.actor_id,
         a1.first_name, a1.last_name,
         a2.first_name, a2.last_name
HAVING COUNT(f1.actor_id) >= 5
ORDER BY shared_films DESC, actor1, actor2
