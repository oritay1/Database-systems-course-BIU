SELECT f1.title AS title1, f2.title AS title2, f1.length, f1.rental_rate, f1.replacement_cost, f1.rating
FROM film AS f1, film AS f2
WHERE f1.title < f2.title 
AND f1.length = f2.length
AND f1.rental_rate = f2.rental_rate
AND f1.replacement_cost = f2.replacement_cost
AND f1.rating = f2.rating
ORDER BY title1