def add_house(conn, c):
    while True:
        postal_code = input("Enter a postal code (or 'done' to exit): ")
        if postal_code == "done":
            break

        c.execute("SELECT * FROM houses WHERE postal_code=?", (postal_code,))
        result = c.fetchone()

        if result is not None:
            print("House already exists in database.")
        else:
            c.execute("INSERT INTO houses (postal_code) VALUES (?)", (postal_code,))
            conn.commit()

    print("Houses added to database successfully!")
