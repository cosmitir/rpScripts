import json


def add_item(conn, c):
    """
    Add items to the database.
    """
    while True:
        name = input("Item Name ('done' to finish): ")
        if not name:
            continue
        if name == "done":
            break

        c.execute("SELECT * FROM items WHERE name=?", (name,))
        result = c.fetchone()

        if result is not None:
            print("Item already exists in database.")
        else:
            c.execute("INSERT INTO items (name) VALUES (?)", (name,))
            conn.commit()
            print("Items added to database successfully!")

    print("Items added to database successfully!")


def search_item(c):
    """
    Search for an item and retrieve the vehicles and houses that have it and their quantities.
    """
    while True:
        item_name = input("Item Name: ")
        if not item_name:
            continue
        break

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


def output_items(c):
    """
    Output the list of items to a JSON file.
    """
    # Retrieve all the items from the database
    c.execute("SELECT * FROM items")
    results = c.fetchall()

    # Convert the data to a dictionary of lists
    data = {}
    for result in results:
        item_id, item_name = result
        data[item_id] = item_name

    # Write the data to a JSON file
    try:
        with open("items.json", "w") as f:
            json.dump(data, f, indent=4)
    except IOError:
        print("Error writing to file.")

    print("Item list output successfully!")
