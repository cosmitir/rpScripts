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
