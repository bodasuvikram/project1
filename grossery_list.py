import os

# Define consistent file path
FILE_NAME = os.path.join(os.path.expanduser("~"), "grocery_list.txt")
print(FILE_NAME)

# Create file if it doesn't exist
if not os.path.exists(FILE_NAME):
    with open(FILE_NAME, "w") as f:
        items = ["milk", "eggs", "curd", "bread", "butter", "candies", "icecream"]
        for i in items:
            f.write(i+ "\n")

last_action = None

# View grocery list
def view_list():
    try:
        with open(FILE_NAME, "r") as file:
            items = file.read().splitlines()
            if items:
                print("Your Grocery List:")
                for item in items:
                    print(item)
            else:
                print("\nYour grocery list is empty.")
    except FileNotFoundError:
        print("\nGrocery list file not found.")

# Add item to the list
def add_item():
    global last_action
    item = input("Enter the item to add: ").lower()
    try:
        with open(FILE_NAME, "r") as file:
            items = file.read().splitlines()
    except FileNotFoundError:
        items = []

    if item in items:
        print(f"{item} already exists in the list.")
    else:
        with open(FILE_NAME, "a") as file:
            file.write(item + "\n")
        last_action = ("add", item)
        print(f"{item} added to the list.")

# Remove item from the list
def remove_item():
    global last_action
    try:
        with open(FILE_NAME, "r") as file:
            items = file.read().splitlines()
    except FileNotFoundError:
        print("Grocery list not found.")
        return

    item = input("Enter the item to remove: ").lower()
    if item in items:
        items.remove(item)
        with open(FILE_NAME, "w") as file:
            for i in items:
                file.write(i + "\n")
        last_action = ("remove", item)
        print(f"{item} removed from the list.")
    else:
        print(f"{item} not found in the list.")

# Search for an item
def search_item():
    try:
        with open(FILE_NAME, "r") as file:
            items = file.read().splitlines()
    except FileNotFoundError:
        print("Grocery list not found.")
        return

    query = input("Enter item to search: ").lower()
    matches = [item for item in items if query in item]
    if matches:
        print("Matching items:")
        for match in matches:
            print("-", match)
    else:
        print("No matching items found.")

# Sort items
def items_sort():
    try:
        with open(FILE_NAME, "r") as file:
            items = file.read().splitlines()
    except FileNotFoundError:
        print("Grocery list not found.")
        return

    if items:
        items.sort()
        print("\nSorted Grocery List:")
        for item in items:
            print("-", item)
    else:
        print("List is empty.")

# Undo last add/remove
def undo(action_info):
    if not action_info:
        print("No action to undo.")
        return

    action, item = action_info
    try:
        with open(FILE_NAME, "r") as file:
            items = file.read().splitlines()
    except FileNotFoundError:
        items = []

    if action == "add" and item in items:
        items.remove(item)
        print(f"Undo complete: Removed {item}")
    elif action == "remove" and item not in items:
        items.append(item)
        print(f"Undo complete: Re-added {item}")

    with open(FILE_NAME, "w") as file:
        for i in items:
            file.write(i + "\n")

# Main loop
while True:
    try:
        user_input = int(input('''
========= Grocery List Menu =========
1. View Grocery List
2. Add Item
3. Remove Item
4. Search Item
5. Sort List
6. Undo Last Action
7. Exit
-------------------------------------
Enter your choice (1-7): '''))
    except ValueError:
        print("❗ Please enter a number between 1 and 7.")
        continue

    if user_input == 1:
        view_list()
    elif user_input == 2:
        add_item()
    elif user_input == 3:
        remove_item()
    elif user_input == 4:
        search_item()
    elif user_input == 5:
        items_sort()
    elif user_input == 6:
        undo(last_action)
    elif user_input == 7:
        print("Exiting Thank you!")
        with open(FILE_NAME, "r") as file:
            items = file.read().splitlines()
            print("Your Grocery List:")
            for item in items:
                print(item)
        break
    else:
        print("! Invalid choice. Please select between 1 and 7.")
