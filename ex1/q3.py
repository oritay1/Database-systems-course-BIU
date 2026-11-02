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
    # first we filter only films with the word 'Documentary' in their description
    # second we also filter the films with the word 'Commentaries' in their special_features field
    # then on the table that returns (in SELECT) we count the film_id collum, we average the length collum and we calculate min / max on the replacement_cost collum
    cursor.execute("""
    SELECT COUNT(film_id) AS num_films , AVG(length) AS avg_length, MIN(replacement_cost) AS min_cost ,MAX(replacement_cost) AS max_cost
    FROM film
    WHERE description LIKE '%Documentary%'
    AND special_features LIKE '%Commentaries%';
    """)
    print(', '.join(str(row) for row in cursor.fetchall()))

    cursor.close()
    mydb.close()