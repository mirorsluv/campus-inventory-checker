# Campus Inventory Tracker

import json
import csv

inventory = inventory = {
    "North Storage": [
        {"item": "Office Chairs", "quantity": 15},
        {"item": "Computer Desks", "quantity": 8},
        {"item": "Storage Boxes", "quantity": 25},
        {"item": "LED Bulbs", "quantity": 3},
        {"item": "Filing Cabinets", "quantity": 6},
        {"item": "Office Tables", "quantity": 12},
        {"item": "Cleaning Supplies", "quantity": 4}
    ],

    "South Storage": [
        {"item": "Computer Monitors", "quantity": 10},
        {"item": "Keyboards", "quantity": 20},
        {"item": "Office Lamps", "quantity": 7},
        {"item": "Printer Paper", "quantity": 2},
        {"item": "Extension Cables", "quantity": 14},
        {"item": "Whiteboards", "quantity": 5},
        {"item": "Desk Organizers", "quantity": 18}
    ]
}
    

def save_inventory():
    with open("inventory.json", "w") as file:
        json.dump(inventory, file, indent=4)


def load_inventory():
    global inventory

    try:
        with open("inventory.json", "r") as file:
            saved_inventory = json.load(file)
            if isinstance(saved_inventory, dict):
                for location, items in saved_inventory.items():
                    if location in inventory and isinstance(items, list):
                        inventory[location] = items 
    except FileNotFoundError:
        save_inventory()

#CALL THE LOAD FUNCTION
load_inventory()     


def view_inventory(location):
    print("\nInventory for", location)
    print("-" * 45)

    for item in inventory[location]:
        print(item["item"], "-", item["quantity"])

        if item["quantity"] < 5:
            print("Warning: Low stock for", item["item"])


def update_quantity(location):
    print("\nUpdate Inventory:", location)

    items = inventory[location]

    for number, item in enumerate(items, start=1):
        print(number, "-", item["item"], ":", item["quantity"])

    choice = int(input("\nEnter the item number to update: "))

    if choice < 1 or choice > len(items):
        print("Invalid item number.")
        return

    new_quantity = int(input("Enter the new quantity: "))

    items[choice - 1]["quantity"] += new_quantity
    save_inventory()

    print("Quantity updated successfully!")
 
def add_item(location):
    print("\nAdd New Inventory Item:", location)

    item_name = input("Enter the item name: ")
    quantity = int(input("Enter the quantity: "))

    new_item = {
        "item": item_name,
        "quantity": quantity
    }

    inventory[location].append(new_item)

    save_inventory()
    print(item_name, "has been added successfully!")

def search_inventory(location):
    search_name = input("\nEnter the item name to search: ").lower()

    found = False

    for item in inventory[location]:
        if search_name in item["item"].lower():
            print("\nItem:", item["item"])
            print("Building:", location)
            print("Quantity:", item["quantity"])
            found = True

    if not found:
        print("Item not found.")

def inventory_summary():
    items = inventory[location]
    total_items = len(items)
    total_quantity = sum(item["quantity"] for item in items)
    low_stock = sum(1 for item in items if item["quantity"] < 5)
    print("\nInventory Summary for", location)
    print("Building:", location) 
    print("Different Items:", total_items)   
    print("Total Quantity:", total_quantity) 
    print("Low Stock Items:", low_stock)
    print("=================================") 

def export_inventory_to_csv(location):
    filename = location.replace(" ", "_") + "_inventory.csv"
    with open(filename, mode='w', newline='') as file:
        writer = csv.writer(file)
        writer.writerow(["Building", "Item", "Quantity"])
        for item in inventory[location]:
            writer.writerow([
                location,
                item["item"],
                item["quantity"]
            ])
    print("Inventory exported successully!")
    print("File saved as:", filename)
    
   
print("\nCAMPUS INVENTORY TRACKER")
print("1. North Storage")
print("2. South Storage")

choice = input("Choose a building (1 or 2): ")

if choice == "1":
    location = "North Storage"
elif choice == "2":
    location = "South Storage"
else:
    print("Invalid choice.")
    exit()

print("\n1. View Inventory")
print("2. Update Quantity")
print("3. Add New Item")
print("4. Search Inventory")
print("5. Inventory Summary")
print("6. Export Inventory to CSV")
action = input("Choose an action: ")

if action == "1":
    view_inventory(location)
elif action == "2":
    update_quantity(location)
elif action == "3":
    add_item(location)
elif action == "4":
    search_inventory(location)
elif action == "5":
    inventory_summary()
elif action == "6":
    export_inventory_to_csv(location)
else:
    print("Invalid action.")

