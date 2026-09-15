import mysql.connector
from mysql.connector import errorcode

import dotenv
from dotenv import dotenv_values

secrets = dotenv_values('../module-5/.env')

# Database config object
config = {
    "user": secrets["USER"],
    "password": secrets["PASSWORD"],
    "host": secrets["HOST"],
    "database": secrets["DATABASE"],
    "raise_on_warnings": True
}
# MySQL: mysql_test.py. Connection test codetry:
# try/catch block for handling potential MySQL dtabase errors
try:
    db = mysql.connector.connect(**config)  # Connect to the movies database
    # # Output the connection status
    # print("\nDatabase user {} connected to MySQL on host {} with database {}".format(
    # config["user"], config["host"], config["database"]))
    # Create cursor
    cursor = db.cursor()

    # INNER JOIN film and studio
    # FROM brings in the film table and JOIN brings the studio table
    # ON provides how to join them - studio_id
    # cursor.execute(
    #     'SELECT film.film_name, studio.studio_name ' 
    #     'FROM film '  
    #     'JOIN studio ON film.studio_id = studio.studio_id'
    # )
    # studio_join_results = cursor.fetchall()
    # print('\n--INNER JOIN film and studio--\n')
    # for result in studio_join_results:
    #     print('Film: {} | Studio Name: {} \n'.format(result[0], result[1]))

    # INNER JOIN film and genre
    # FROM brings in the film table and JOIN brings the genre table
    # ON provides how to join them - genre_id
    cursor.execute(
        'SELECT film.film_name, genre.genre_name '
        'FROM film '
        'JOIN genre ON film.genre_id = genre.genre_id'
    )
    genre_join_results = cursor.fetchall()
    print('\n--INNER JOIN film and genre--\n')
    for result in genre_join_results:
        print('Film: {} | Genre: {} \n'.format(result[0], result[1]))


except mysql.connector.Error as err:
    # On error code
    if err.errno == errorcode.ER_ACCESS_DENIED_ERROR:
        print("The supplied username or password are invalid")
    elif err.errno == errorcode.ER_BAD_DB_ERROR:
        print("The specified database does not exist")
    else:
        print(err)
finally:
    # Close the connection
    db.close()
