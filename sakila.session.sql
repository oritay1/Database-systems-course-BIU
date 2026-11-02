SELECT cust.customer_id, first_name,last_name,rental_id,rental.inventory_id,inventory.film_id, film.rating,film_category.category_id, category.name
FROM customer AS cust, rental, inventory, film ,film_category ,category
WHERE cust.customer_id = rental.customer_id
AND rental.inventory_id = inventory.inventory_id
AND inventory.film_id = film.film_id
AND film.rating = 'NC-17'
AND film.film_id = film_category.film_id
AND film_category.category_id = category.category_id
AND category.name = 'Horror'

UNION

SELECT cust.customer_id, first_name,last_name,rental_id,rental.inventory_id,inventory.film_id, film.rating,film_category.category_id, category.name
FROM customer AS cust, rental, inventory, film ,film_category ,category
WHERE cust.customer_id = rental.customer_id
AND rental.inventory_id = inventory.inventory_id
AND inventory.film_id = film.film_id
AND film.rating = 'G'
AND film.film_id = film_category.film_id
AND film_category.category_id = category.category_id
AND category.name = 'Music'

SELECT *
FROM rental

SELECT *
FROM inventory

SELECT *
FROM film

SELECT *
FROM category

SELECT *
FROM film_category

SELECT *
FROM rental as r1, rental as r2
WHERE r1.customer_id = r2.customer_id
AND r1.rental_id < r2.rental_id





SELECT cust.customer_id, first_name,last_name
FROM customer AS cust, rental, inventory, film ,film_category ,category
WHERE cust.customer_id = rental.customer_id
AND rental.inventory_id = inventory.inventory_id
AND inventory.film_id = film.film_id
AND film.rating = 'NC-17'
AND film.film_id = film_category.film_id
AND film_category.category_id = category.category_id
AND category.name = 'Horror'

INTERSECT

SELECT cust.customer_id, first_name,last_name
FROM customer AS cust, rental, inventory, film ,film_category ,category
WHERE cust.customer_id = rental.customer_id
AND rental.inventory_id = inventory.inventory_id
AND inventory.film_id = film.film_id
AND film.rating = 'G'
AND film.film_id = film_category.film_id
AND film_category.category_id = category.category_id
AND category.name = 'Music'
ORDER BY customer_id