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
    # We use INTERSECT between two queries.
    # We first take the customers that bought a Horror movie with PG-17 rating
    # We second calculate the customers that bought a Music movie with G rating
    # The intersection between those 2 sets gives the set of:

    # customers that bought a Horror movie with PG-17 rating
    # AND
    # the customers that bought a Music movie with G rating
    
    # Then sort
    cursor.execute("""
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
    ORDER BY customer_id;
    """)
    print(', '.join(str(row) for row in cursor.fetchall()))

    cursor.close()
    mydb.close()