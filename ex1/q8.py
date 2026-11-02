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
    # We use UNION between two queries.
    # We first take the names of actors that starts with WIL in their last name
    # Then we take the names of customers that starts with WIL in their last name
    # Then we preform UNION between them so we dont have duplicate names
    # Then sort
    cursor.execute("""
    SELECT first_name, last_name
    FROM actor
    WHERE actor.last_name LIKE 'WIL%'

    UNION

    SELECT first_name, last_name
    FROM customer
    WHERE customer.last_name LIKE 'WIL%'

    ORDER BY last_name, first_name;
    """)
    print(', '.join(str(row) for row in cursor.fetchall()))

    cursor.close()
    mydb.close()