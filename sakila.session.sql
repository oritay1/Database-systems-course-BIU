SELECT actor.actor_id, actor.first_name,actor.last_name
FROM actor, film_actor, film_category, category
WHERE actor.actor_id = film_actor.actor_id
AND film_actor.film_id = film_category.film_id
AND film_category.category_id = category.category_id
AND category.name = 'Action'

EXCEPT

SELECT actor.actor_id, actor.first_name,actor.last_name
FROM actor, film_actor, film_category, category
WHERE actor.actor_id = film_actor.actor_id
AND film_actor.film_id = film_category.film_id
AND film_category.category_id = category.category_id
AND category.name = 'Drama'
ORDER BY last_name, first_name, actor_id