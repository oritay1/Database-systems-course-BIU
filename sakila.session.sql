SELECT DISTINCT first_name
FROM customer
WHERE active = 1
AND first_name LIKE '_A__'
ORDER BY first_name
