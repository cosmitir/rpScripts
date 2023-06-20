# Import statements go at the top of the file
import os


def menu():
    """Prints a menu for the user to select from."""
    input(
        "Press Enter to continue..."
    )  # Wait for user input before clearing the console
    os.system("cls" if os.name == "nt" else "clear")  # Clear the console

    print("Select an option:")
    print("+----+-----------------------------+")
    print("| 1. | Add a new vehicle to database |")
    print("| 2. | Add a new house to database   |")
    print("| 3. | Add a new item to database    |")
    print("| 4. | Add items to a vehicle        |")
    print("| 5. | Add items to a house          |")
    print("| 6. | Remove items from a vehicle   |")
    print("| 7. | Remove items from a house     |")
    print("| 8. | Search for an item            |")
    print("| 9. | Output the database           |")
    print("| 10.| Output item list              |")
    print("| 0. | Exit                          |")
    print("+----+-----------------------------+")
