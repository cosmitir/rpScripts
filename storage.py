# Import the necessary libraries
import sqlite3

from config import database_path, options_conn_c, options_c
from database import create_tables
from menu import menu


def main():
    # Connect to the database
    conn, c = connect()  # type: ignore

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


def connect():
    try:
        conn = sqlite3.connect(database_path)
        c = conn.cursor()
    except sqlite3.Error as e:
        print(f"Error connecting to database: {e}")
        return

    return conn, c


if __name__ == "__main__":
    main()
