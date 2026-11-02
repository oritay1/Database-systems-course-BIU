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
    # We use self-join here
    # We first filter self-tuples and we keep only one type of tuple ( for example we only keep [x,y] and filter [y,x] by using the operator '<')
    # Then filter the films using question conditions (length, rental_rate, replacement_cost,rating)
    # Then we sort by title1
    cursor.execute("""
    SELECT f1.title AS title1, f2.title AS title2, f1.length, f1.rental_rate, f1.replacement_cost, f1.rating
    FROM film AS f1, film AS f2
    WHERE f1.title < f2.title 
    AND f1.length = f2.length
    AND f1.rental_rate = f2.rental_rate
    AND f1.replacement_cost = f2.replacement_cost
    AND f1.rating = f2.rating
    ORDER BY title1;
    """)
    print(', '.join(str(row) for row in cursor.fetchall()))

    cursor.close()
    mydb.close()