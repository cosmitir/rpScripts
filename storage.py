import sqlite3
import os

from database import create_tables, output_database
from vehicle import add_vehicle, add_items_to_vehicle, remove_items_from_vehicle
from house import add_house, add_items_to_house, remove_items_from_house
from item import add_item, search_item, output_items


options_conn_c = {
    "1": add_vehicle,
    "2": add_house,
    "3": add_item,
    "4": add_items_to_vehicle,
    "5": add_items_to_house,
    "6": remove_items_from_vehicle,
    "7": remove_items_from_house,
}

options_c = {
    "8": search_item,
    "9": output_database,
    "10": output_items,
}


def main():
    # Connect to the database
    conn = sqlite3.connect("D:/storage/database/vehicles/vehicles.db")
    c = conn.cursor()

    # Create the table
    create_tables(conn, c)

    while True:
        input(
            "Press Enter to continue..."
        )  # Wait for user input before clearing the console
        os.system("cls" if os.name == "nt" else "clear")  # Clear the console

        print("Select an option:")
        print("1. Add vehicles to database")
        print("2. Add houses to database")
        print("3. Add items to database")
        print("4. Add items to a vehicle")
        print("5. Add items to an house")
        print("6. Remove items from a vehicle")
        print("7. Remove items from an house")
        print("8. Search for an item")
        print("9. Output the database")
        print("10. Output item list")
        print("0. Exit")

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
