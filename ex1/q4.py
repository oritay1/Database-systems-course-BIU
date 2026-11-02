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
    # The path to the category name is: film.film_id -> film_category.category_id -> category.category_id
    # That is why we join 3 tables: film , film.category , category and we filter them correctly according to the path
    # Then we Group by category.category_id
    # Then we filter by the question conditions using 'HAVING'
    # And at the end we sort
    cursor.execute("""
    SELECT category.name AS category ,COUNT(*) AS num_films, AVG(length) AS avg_length
    FROM film, film_category,category
    WHERE film.film_id = film_category.film_id
    AND category.category_id = film_category.category_id
    GROUP BY category.category_id
    HAVING COUNT(*) >= 60
    AND AVG(length) > 110
    ORDER BY avg_length DESC;
    """)
    print(', '.join(str(row) for row in cursor.fetchall()))

    cursor.close()
    mydb.close()