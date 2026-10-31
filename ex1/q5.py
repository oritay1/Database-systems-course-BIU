import mysql.connector
if __name__ == '__main__':
    mydb = mysql.connector.connect(
        host="localhost",
        user="root",
        password="root",
        database="sakila",
        port="3307",
    )
    cursor = mydb.cursor()
    # The idea is: 
    # We join 2 tables: customer and payment
    # We first filter the matching lines according to: customer.customer_id = payment.customer_id
    # Then we group by the id and name
    # Then we filter the result according to the question conditions
    # Then we sort by num_payments (if there is equality we break it by sorting by customer_id) 
    cursor.execute("""
    SELECT customer.customer_id, first_name, last_name , COUNT(*) AS num_payments, SUM(payment.amount) AS total_paid
    FROM customer, payment
    WHERE customer.customer_id = payment.customer_id
    GROUP BY customer.customer_id, customer.first_name,customer.last_name
    HAVING COUNT(*) >= 35
    AND SUM(payment.amount) >= 175
    ORDER BY num_payments DESC, customer.customer_id ASC
    """)
    print(', '.join(str(row) for row in cursor.fetchall()))

    cursor.close()
    mydb.close()