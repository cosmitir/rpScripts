import sqlite3
import os
import json

from vehicle import add_vehicle
from house import add_house
from item import add_item

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


def add_items_to_vehicle(license_plate):
    vehicle_id = get_vehicle_id(license_plate)
    if vehicle_id:
        items = []
        while True:
            item_name = input("Enter the item name (or 'done' to finish): ")
            if item_name == "done":
                break
            item_quantity = int(input("Enter the quantity: "))
            item_id = get_item_id(item_name)
            if item_id:
                items.append((item_id, item_quantity))
            else:
                print(f"Item '{item_name}' does not exist in the database.")
        for item in items:
            item_id, item_quantity = item
            # Check if the item already exists in the vehicle's trunk
            c.execute(
                "SELECT * FROM vehicle_items WHERE vehicle_id = ? AND item_id = ?",
                (vehicle_id, item_id),
            )
            existing_item = c.fetchone()
            if existing_item:
                # If the item exists, update the quantity
                quantity = existing_item[2] + item_quantity
                c.execute(
                    "UPDATE vehicle_items SET quantity = ? WHERE vehicle_id = ? AND item_id = ?",
                    (quantity, vehicle_id, item_id),
                )
            else:
                # If the item doesn't exist, insert a new row
                c.execute(
                    "INSERT INTO vehicle_items (vehicle_id, item_id, quantity) VALUES (?, ?, ?)",
                    (vehicle_id, item_id, item_quantity),
                )
        conn.commit()
        print("Items added to vehicle successfully!")
    else:
        print(
            f"Vehicle with license plate '{license_plate}' does not exist in the database."
        )


def add_items_to_house(postal_code):
    house_id = get_house_id(postal_code)
    if house_id:
        items = []
        while True:
            item_name = input("Enter the item name (or 'done' to finish): ")
            if item_name == "done":
                break
            item_quantity = int(input("Enter the quantity: "))
            item_id = get_item_id(item_name)
            if item_id:
                items.append((item_id, item_quantity))
            else:
                print(f"Item '{item_name}' does not exist in the database.")
        for item in items:
            item_id, item_quantity = item
            # Check if the item already exists in the house's storage
            c.execute(
                "SELECT * FROM house_items WHERE house_id = ? AND item_id = ?",
                (house_id, item_id),
            )
            existing_item = c.fetchone()
            if existing_item:
                # If the item exists, update the quantity
                quantity = existing_item[2] + item_quantity
                c.execute(
                    "UPDATE house_items SET quantity = ? WHERE house_id = ? AND item_id = ?",
                    (quantity, house_id, item_id),
                )
            else:
                # If the item doesn't exist, insert a new row
                c.execute(
                    "INSERT INTO house_items (house_id, item_id, quantity) VALUES (?, ?, ?)",
                    (house_id, item_id, item_quantity),
                )
        conn.commit()
        print("Items added to house successfully!")
    else:
        print(f"House with postal code '{postal_code}' does not exist in the database.")


def remove_items_from_vehicle(license_plate):
    vehicle_id = get_vehicle_id(license_plate)
    if vehicle_id:
        items = []
        while True:
            item_name = input("Enter the item name (or 'done' to finish): ")
            if item_name == "done":
                break
            item_quantity = int(input("Enter the quantity: "))
            item_id = get_item_id(item_name)
            if item_id:
                items.append((item_id, item_quantity))
            else:
                print(f"Item '{item_name}' does not exist in the database.")
        for item in items:
            item_id, item_quantity = item
            # Check if the item exists in the vehicle's trunk
            c.execute(
                "SELECT * FROM vehicle_items WHERE vehicle_id = ? AND item_id = ?",
                (vehicle_id, item_id),
            )
            existing_item = c.fetchone()
            if existing_item:
                # If the item exists, decrement the quantity
                quantity = existing_item[2] - item_quantity
                if quantity <= 0:
                    # If the quantity reaches 0, remove the item from the vehicle's trunk
                    c.execute(
                        "DELETE FROM vehicle_items WHERE vehicle_id = ? AND item_id = ?",
                        (vehicle_id, item_id),
                    )
                else:
                    c.execute(
                        "UPDATE vehicle_items SET quantity = ? WHERE vehicle_id = ? AND item_id = ?",
                        (quantity, vehicle_id, item_id),
                    )
            else:
                print(f"Item '{item_name}' does not exist in the vehicle's trunk.")
        conn.commit()
        print("Items removed from vehicle successfully!")
    else:
        print(
            f"Vehicle with license plate '{license_plate}' does not exist in the database."
        )


def remove_items_from_house(postal_code):
    house_id = get_house_id(postal_code)
    if house_id:
        items = []
        while True:
            item_name = input("Enter the item name (or 'done' to finish): ")
            if item_name == "done":
                break
            item_quantity = int(input("Enter the quantity: "))
            item_id = get_item_id(item_name)
            if item_id:
                items.append((item_id, item_quantity))
            else:
                print(f"Item '{item_name}' does not exist in the database.")
        for item in items:
            item_id, item_quantity = item
            # Check if the item exists in the house's storage
            c.execute(
                "SELECT * FROM house_items WHERE house_id = ? AND item_id = ?",
                (house_id, item_id),
            )
            existing_item = c.fetchone()
            if existing_item:
                # If the item exists, decrement the quantity
                quantity = existing_item[2] - item_quantity
                if quantity <= 0:
                    # If the quantity reaches 0, remove the item from the house's storage
                    c.execute(
                        "DELETE FROM house_items WHERE house_id = ? AND item_id = ?",
                        (house_id, item_id),
                    )
                else:
                    c.execute(
                        "UPDATE house_items SET quantity = ? WHERE house_id = ? AND item_id = ?",
                        (quantity, house_id, item_id),
                    )
            else:
                print(f"Item '{item_name}' does not exist in the house's storage.")
        conn.commit()
        print("Items removed from house successfully!")
    else:
        print(f"House with postal code '{postal_code}' does not exist in the database.")


def search_item(item_name):
    # Search for an item and retrieve the vehicles and houses that have it and their quantities
    c.execute(
        f"""SELECT vehicles.license_plate, vehicle_items.quantity
                 FROM vehicles
                 INNER JOIN vehicle_items ON vehicles.id = vehicle_items.vehicle_id
                 INNER JOIN items ON vehicle_items.item_id = items.id
                 WHERE items.name = ?
                 UNION
                 SELECT houses.postal_code, house_items.quantity
                 FROM houses
                 INNER JOIN house_items ON houses.id = house_items.house_id
                 INNER JOIN items ON house_items.item_id = items.id
                 WHERE items.name = ?
                 ORDER BY quantity DESC""",
        (item_name, item_name),
    )
    results = c.fetchall()
    if results:
        print(f"Vehicles and houses with item '{item_name}':")
        for result in results:
            identifier, quantity = result
            print(f"{identifier} | {quantity}")
    else:
        print(f"No vehicles or houses have item '{item_name}'.")


def output_database():
    # Retrieve all the data from the database
    c.execute(
        """SELECT vehicles.license_plate, items.name, vehicle_items.quantity
                 FROM vehicles
                 INNER JOIN vehicle_items ON vehicles.id = vehicle_items.vehicle_id
                 INNER JOIN items ON vehicle_items.item_id = items.id
                 UNION
                 SELECT houses.postal_code, items.name, house_items.quantity
                 FROM houses
                 INNER JOIN house_items ON houses.id = house_items.house_id
                 INNER JOIN items ON house_items.item_id = items.id"""
    )
    results = c.fetchall()

    # Convert the data to a dictionary of lists
    data = {}
    for result in results:
        identifier, item_name, quantity = result
        if identifier not in data:
            data[identifier] = []
        data[identifier].append({item_name: quantity})

    # Write the data to a JSON file
    with open("output.json", "w") as f:
        json.dump(data, f, indent=4)


def output_items():
    # Retrieve all the items from the database
    c.execute("SELECT * FROM items")
    results = c.fetchall()

    # Convert the data to a dictionary of lists
    data = {}
    for result in results:
        item_id, item_name = result
        data[item_id] = item_name

    # Write the data to a JSON file
    with open("items.json", "w") as f:
        json.dump(data, f, indent=4)


def get_vehicle_id(license_plate):
    # Retrieve the vehicle ID based on the license plate
    c.execute("SELECT id FROM vehicles WHERE license_plate = ?", (license_plate,))
    result = c.fetchone()
    if result:
        return result[0]
    else:
        return None


def get_house_id(postal_code):
    # Retrieve the house ID based on the postal code
    c.execute("SELECT id FROM houses WHERE postal_code = ?", (postal_code,))
    result = c.fetchone()
    if result:
        return result[0]
    else:
        return None


def get_item_id(name):
    # Retrieve the item ID based on the item name
    c.execute("SELECT id FROM items WHERE name = ?", (name,))
    result = c.fetchone()
    if result:
        return result[0]
    else:
        return None


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
        license_plate = input("Enter the license plate of the vehicle: ")
        add_items_to_vehicle(license_plate)
    elif option == "5":
        postal_code = input("Enter the postal code of the house: ")
        add_items_to_house(postal_code)
    elif option == "6":
        license_plate = input("Enter the license plate of the vehicle: ")
        remove_items_from_vehicle(license_plate)
    elif option == "7":
        postal_code = input("Enter the postal code of the house: ")
        remove_items_from_house(postal_code)
    elif option == "8":
        item_name = input("Enter the item name: ")
        search_item(item_name)
    elif option == "9":
        output_database()
        print("Database output successfully!")
    elif option == "10":
        output_items()
        print("Item list output successfully!")
    elif option == "0":
        break
    else:
        print("Invalid option. Please try again.")

# Close the database connection
conn.close()
