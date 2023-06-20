from get_id import get_house_id, get_item_id


def add_house(conn, c):
    while True:
        postal_code = input("Postal Code ('done' to exit): ")
        if not postal_code:
            continue
        if postal_code == "done":
            break

        # Check if the house already exists in the database
        c.execute("SELECT * FROM houses WHERE postal_code=?", (postal_code,))
        result = c.fetchone()

        if result is not None:
            print("House already exists in database.")
        else:
            # Insert the new house into the database
            c.execute("INSERT INTO houses (postal_code) VALUES (?)", (postal_code,))
            conn.commit()

    print("Houses added to database successfully!")


def add_items_to_house(conn, c):
    while True:
        postal_code = input("Postal Code: ")
        if not postal_code:
            continue
        break
    house_id = get_house_id(c, postal_code)
    if house_id:
        items = []
        while True:
            item_name = input("Item Name ('done' to finish): ")
            if not item_name:
                continue
            if item_name == "done":
                break
            try:
                item_quantity = int(input("Enter the quantity: "))
            except ValueError:
                print("Invalid quantity. Please enter a number.")
                continue
            item_id = get_item_id(c, item_name)
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


def remove_items_from_house(conn, c):
    while True:
        postal_code = input("Postal Code: ")
        if not postal_code:
            continue
        break
    house_id = get_house_id(c, postal_code)
    if house_id:
        items = []
        while True:
            item_name = input("Item Name ('done' to finish): ")
            if not item_name:
                continue
            if item_name == "done":
                break
            try:
                item_quantity = int(input("Enter the quantity: "))
            except ValueError:
                print("Invalid quantity. Please enter a number.")
                continue
            item_id = get_item_id(c, item_name)
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
