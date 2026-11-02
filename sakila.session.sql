SELECT first_name, last_name
FROM actor
WHERE actor.last_name LIKE 'WIL%'

UNION

SELECT first_name, last_name
FROM customer
WHERE customer.last_name LIKE 'WIL%'

ORDER BY last_name, first_name