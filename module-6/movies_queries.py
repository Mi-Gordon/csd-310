import mysql.connector
from mysql.connector import errorcode

import dotenv
from dotenv import dotenv_values

# Using the .env file
secrets = dotenv_values("../module-5/.env")

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
    #     config["user"], config["host"], config["database"]))

    # Create cursor
    cursor = db.cursor()

    # First query
    cursor.execute("SELECT * FROM studio")
    studio_results = cursor.fetchall()

    print('\n-- DISPLAYING Studio RECORDS --')
    # Loop though each result
    for studio in studio_results:
        print("Studio ID: {}\nStudio Name: {}\n".format(studio[0], studio[1]))

    # Second query
    cursor.execute("SELECT * FROM genre")
    genre_results = cursor.fetchall()

    print("\n-- DISPLAYING Genre RECORDS --")
    # Loop through each result
    for genre in genre_results:
        print("Genre ID: {}\nGenre Name: {}\n".format(genre[0], genre[1]))

    # Third query
    cursor.execute(
        "SELECT film_name, film_runtime FROM film WHERE film_runtime < 120")
    runtime_results = cursor.fetchall()

    print("\n-- DISPLAYING Short Film RECORDS --")
    # Loop through each result
    for film in runtime_results:
        print("Film Name: {}\nRuntime: {}\n".format(film[0], film[1]))

    # Fourth query
    cursor.execute(
        "SELECT film_name, film_director FROM film GROUP BY film_director")
    director_results = cursor.fetchall()

    print("\n-- DISPLAYING Director RECORDS in Order --")
    # Loop through each result
    for film in director_results:
        print("Film Name: {}\nDirector: {}\n".format(film[0], film[1]))

    input("\nPress any key to continue...")

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
