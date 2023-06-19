def get_vehicle_id(c, license_plate):
    # Retrieve the vehicle ID based on the license plate
    c.execute("SELECT id FROM vehicles WHERE license_plate = ?", (license_plate,))
    result = c.fetchone()
    if result:
        return result[0]
    else:
        raise ValueError("No vehicle found with license plate {}".format(license_plate))


def get_house_id(c, postal_code):
    # Retrieve the house ID based on the postal code
    c.execute("SELECT id FROM houses WHERE postal_code = ?", (postal_code,))
    result = c.fetchone()
    if result:
        return result[0]
    else:
        raise ValueError("No house found with postal code {}".format(postal_code))


def get_item_id(c, name):
    # Retrieve the item ID based on the item name
    c.execute("SELECT id FROM items WHERE name = ?", (name,))
    result = c.fetchone()
    if result:
        return result[0]
    else:
        raise ValueError("No item found with name {}".format(name))
