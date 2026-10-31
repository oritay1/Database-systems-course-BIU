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
    # first we filter by rating
    # second and third by the condition 100 <= length <= 120
    # forth by rental rate
    # and last we order by length and if needed by title
    cursor.execute("""
    SELECT title, rating, length, replacement_cost
    FROM film
    WHERE rating = 'PG-13'
    AND length >= 100
    AND length <= 120
    AND rental_rate < 3
    ORDER BY length DESC, title
    """)
    print(', '.join(str(row) for row in cursor.fetchall()))

    cursor.close()
    mydb.close()