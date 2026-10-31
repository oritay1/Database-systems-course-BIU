SELECT customer.customer_id, first_name, last_name , COUNT(*) AS num_payments, SUM(payment.amount) AS total_paid
FROM customer, payment
WHERE customer.customer_id = payment.customer_id
GROUP BY customer.customer_id, customer.first_name,customer.last_name
HAVING COUNT(*) >= 35
AND SUM(payment.amount) >= 175
ORDER BY num_payments DESC, customer.customer_id ASC

