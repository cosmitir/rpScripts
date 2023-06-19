import os


def menu():
    input(
        "Press Enter to continue..."
    )  # Wait for user input before clearing the console
    os.system("cls" if os.name == "nt" else "clear")  # Clear the console

    print("Select an option:")
    print("1. Add vehicles to database")
    print("2. Add houses to database")
    print("3. Add items to database")
    print("4. Add items to a vehicle")
    print("5. Add items to an house")
    print("6. Remove items from a vehicle")
    print("7. Remove items from an house")
    print("8. Search for an item")
    print("9. Output the database")
    print("10. Output item list")
    print("0. Exit")
