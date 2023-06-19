import json


def output_database(c):
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
