from database import output_database
from vehicle import add_vehicle, add_items_to_vehicle, remove_items_from_vehicle
from house import add_house, add_items_to_house, remove_items_from_house
from item import add_item, search_item, output_items

database_path = "D:/storage/database/vehicles/vehicles.db"

options_conn_c = {
    "1": add_vehicle,
    "2": add_house,
    "3": add_item,
    "4": add_items_to_vehicle,
    "5": add_items_to_house,
    "6": remove_items_from_vehicle,
    "7": remove_items_from_house,
}

options_c = {
    "8": search_item,
    "9": output_database,
    "10": output_items,
}
