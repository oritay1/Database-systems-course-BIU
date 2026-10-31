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
    # first we filter only customerts with active = 1
    # second we filter customers with a 4 letter name that matches the pattern: _ A _ _
    # note: the letter _ represent a single letter
    # We use the LIKE operator instead of '='
    cursor.execute("""
    SELECT DISTINCT first_name
    FROM customer
    WHERE active = 1
    AND first_name LIKE '_A__'
    ORDER BY first_name
    """)
    print(', '.join(str(row) for row in cursor.fetchall()))

    cursor.close()
    mydb.close()