import sqlite3
import os

from config import database, options_conn_c, options_c
from database import create_tables
from menu import menu


def main():
    # Connect to the database
    conn = sqlite3.connect(database)
    c = conn.cursor()

    # Create the tables
    create_tables(conn, c)

    while True:
        menu()

        option = input("Enter the option number: ")

        if option == "0":
            break

        if option in options_conn_c:
            options_conn_c[option](conn, c)
        elif option in options_c:
            options_c[option](c)
        else:
            print("Invalid option. Please try again.")

    # Close the database connection
    conn.close()


if __name__ == "__main__":
    main()
