import sqlite3
import os
import json

from database import output_database
from vehicle import add_vehicle, add_items_to_vehicle, remove_items_from_vehicle
from house import add_house, add_items_to_house, remove_items_from_house
from item import add_item, search_item, output_items

# Connect to the database
conn = sqlite3.connect("D:/storage/database/vehicles/vehicles.db")
c = conn.cursor()

# Create the vehicles table if it doesn't exist
c.execute(
    """CREATE TABLE IF NOT EXISTS vehicles (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                license_plate TEXT NOT NULL
             )"""
)

# Create the vehicles table if it doesn't exist
c.execute(
    """CREATE TABLE IF NOT EXISTS houses (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                postal_code TEXT NOT NULL
             )"""
)

# Create the items table if it doesn't exist
c.execute(
    """CREATE TABLE IF NOT EXISTS items (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                name TEXT NOT NULL
             )"""
)

# Create the vehicle_items table if it doesn't exist
c.execute(
    """CREATE TABLE IF NOT EXISTS vehicle_items (
                vehicle_id INTEGER,
                item_id INTEGER,
                quantity INTEGER,
                FOREIGN KEY (vehicle_id) REFERENCES vehicles (id),
                FOREIGN KEY (item_id) REFERENCES items (id)
             )"""
)

# Create the house_items table if it doesn't exist
c.execute(
    """CREATE TABLE IF NOT EXISTS house_items (
								house_id INTEGER,
								item_id INTEGER,
								quantity INTEGER,
								FOREIGN KEY (house_id) REFERENCES houses (id),
								FOREIGN KEY (item_id) REFERENCES items (id)
						 )"""
)


# Usage examples
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

    if option == "1":
        add_vehicle(conn, c)
    elif option == "2":
        add_house(conn, c)
    elif option == "3":
        add_item(conn, c)
    elif option == "4":
        add_items_to_vehicle(conn, c)
    elif option == "5":
        add_items_to_house(conn, c)
    elif option == "6":
        remove_items_from_vehicle(conn, c)
    elif option == "7":
        remove_items_from_house(conn, c)
    elif option == "8":
        search_item(c)
    elif option == "9":
        output_database(c)
    elif option == "10":
        output_items(c)
    elif option == "0":
        break
    else:
        print("Invalid option. Please try again.")

# Close the database connection
conn.close()
