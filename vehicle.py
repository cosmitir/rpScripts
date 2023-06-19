from get_id import get_vehicle_id, get_item_id


def add_vehicle(conn, c):
    while True:
        license_plate = input("License Plate ('done' to exit): ")
        if license_plate == "done":
            break

        c.execute("SELECT * FROM vehicles WHERE license_plate=?", (license_plate,))
        result = c.fetchone()

        if result is not None:
            print("Vehicle already exists in database.")
        else:
            c.execute(
                "INSERT INTO vehicles (license_plate) VALUES (?)", (license_plate,)
            )
            conn.commit()

    print("Vehicles added to database successfully!")


def add_items_to_vehicle(conn, c):
    license_plate = input("Enter the license plate of the vehicle: ")
    vehicle_id = get_vehicle_id(c, license_plate)
    if vehicle_id:
        items = []
        while True:
            item_name = input("Enter the item name (or 'done' to finish): ")
            if item_name == "done":
                break
            item_quantity = int(input("Enter the quantity: "))
            item_id = get_item_id(c, item_name)
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


def remove_items_from_vehicle(conn, c):
    license_plate = input("Enter the license plate of the vehicle: ")
    vehicle_id = get_vehicle_id(c, license_plate)
    if vehicle_id:
        items = []
        while True:
            item_name = input("Enter the item name (or 'done' to finish): ")
            if item_name == "done":
                break
            item_quantity = int(input("Enter the quantity: "))
            item_id = get_item_id(c, item_name)
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
