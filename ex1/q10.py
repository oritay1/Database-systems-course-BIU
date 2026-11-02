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
    # We use EXCEPT between two queries (this operator is like set minus we leant in Bdida course on first year).
    # We first take the actors that played in an Action movie
    # We second take the actors that played in an Drama movie
    # The preforming EXCEPT between those 2 sets gives the set of:
    # actors that played in an Action movie BUT NOT actors that played in an Drama movie
    
    # Then sort
    cursor.execute("""
    SELECT actor.actor_id, actor.first_name,actor.last_name
    FROM actor, film_actor, film_category, category
    WHERE actor.actor_id = film_actor.actor_id
    AND film_actor.film_id = film_category.film_id
    AND film_category.category_id = category.category_id
    AND category.name = 'Action'

    EXCEPT

    SELECT actor.actor_id, actor.first_name,actor.last_name
    FROM actor, film_actor, film_category, category
    WHERE actor.actor_id = film_actor.actor_id
    AND film_actor.film_id = film_category.film_id
    AND film_category.category_id = category.category_id
    AND category.name = 'Drama'
    ORDER BY last_name, first_name, actor_id;
    """)
    print(', '.join(str(row) for row in cursor.fetchall()))

    cursor.close()
    mydb.close()