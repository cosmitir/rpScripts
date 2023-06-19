def add_item(conn, c):
    while True:
        name = input("Enter an item name (or 'done' to exit): ")
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
