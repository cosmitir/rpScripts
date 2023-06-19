import sqlite3

from config import database, options_conn_c, options_c
from database import create_tables
from menu import menu


def main():
    # Connect to the database
    try:
        conn = sqlite3.connect(database)
        c = conn.cursor()
    except sqlite3.Error as e:
        print(f"Error connecting to database: {e}")
        return

    # Create the tables
    try:
        create_tables(conn, c)
    except sqlite3.Error as e:
        print(f"Error creating tables: {e}")
        conn.close()
        return

    while True:
        menu()

        option = input("Enter the option number: ")

        if option == "0":
            break

        if option in options_conn_c:
            try:
                options_conn_c[option](conn, c)
            except sqlite3.Error as e:
                print(f"Error executing command: {e}")
        elif option in options_c:
            try:
                options_c[option](c)
            except sqlite3.Error as e:
                print(f"Error executing command: {e}")
        else:
            print("Invalid option. Please try again.")

    # Close the database connection
    conn.close()


if __name__ == "__main__":
    main()
