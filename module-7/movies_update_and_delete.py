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


def show_films(cursor, title):
    # Method to execute an inner join on all tables, iterate over the dataset and output the results to the terminal window

    # INNER JOIN query
    cursor.execute("SELECT film_name AS Name, "
                   "film_director AS Director, "
                   "genre_name AS Genre, "
                   "studio_name AS 'Studio Name' "
                   "FROM film "
                   "INNER JOIN genre "
                   "ON film.genre_id = genre.genre_id "
                   "INNER JOIN studio "
                   "ON film.studio_id = studio.studio_id")

    # Get the results from the cursor object
    films = cursor.fetchall()

    print('\n -- {} --'.format(title))

    # Iterate over the film data set and display the results
    for film in films:
        print('Film Name: {}\n'
              'Director: {}\n'
              'Genre Name: {}\n'
              'Studio Name: {}\n'.format(film[0], film[1], film[2], film[3]))


# MySQL: mysql_test.py. Connection test codetry:
# try/catch block for handling potential MySQL dtabase errors
try:
    db = mysql.connector.connect(**config)  # Connect to the movies database
    # Create cursor
    cursor = db.cursor()

    show_films(cursor, "DISPLAYING FILMS AFTER DELETE")

    # # INNER JOIN film and genre
    # # FROM brings in the film table and JOIN brings the genre table
    # # ON provides how to join them - genre_id
    # cursor.execute(
    #     'SELECT film.film_name, genre.genre_name '
    #     'FROM film '
    #     'JOIN genre ON film.genre_id = genre.genre_id'
    # )
    # genre_join_results = cursor.fetchall()
    # print('\n--INNER JOIN film and genre--\n')
    # for result in genre_join_results:
    #     print('Film: {} | Genre: {} \n'.format(result[0], result[1]))


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
