import json


def create_tables(conn, c):
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

    conn.commit()


def output_database(c):
    try:
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

        print("Database output successfully!")
    except Exception as e:
        print(f"An error occurred: {e}")
