from menu_item import MenuItem,connection
from menu_manager import MenuManager

def show_user_menu():
    while True:
        print("Program Menu:")
        print("V - View an Item")
        print("A - Add an Item")
        print("D - Delete an Item")
        print("U - Update an Item")
        print("S - Show the Menu")
        print("E - Exit Program")

        choice = input("Enter your choice: ").strip().lower()

        if choice == 'v':
            pass
        elif choice == 'a':
            add_item_to_menu()
        elif choice == 'd':
            remove_item_from_menu()
        elif choice == 'u':
            update_item_from_menu()
        elif choice == 's':
            show_restaurant_menu()
            break
        elif choice == 'e':
            print("Restaurant Menu:")
            show_restaurant_menu()
            print("Exiting the program.")
            break
        else:
            print("Invalid choice. Please try again.")
            
            
def add_item_to_menu():
    name = input("Enter the item's name: ")
    price = int(input("Enter the item's price: "))

    item = MenuItem(name, price)
    item.save()

    print(f"Item '{name}' with price {price} was added successfully.")
    
def remove_item_from_menu():
    name = input("Enter the name of the item you want to remove: ")
    item = MenuItem()
    item.delete(name)

    print(f"Item '{name}' was deleted successfully.")
    
def update_item_from_menu():
    new_name = input("Enter the new name for the item: ")
    new_price = int(input("Enter the new price for the item: "))
    old_name = input("Enter the name of the item you want to update: ")

    item = MenuItem()
    item.update(new_name, new_price, old_name)

    print(f"Item '{old_name}' was updated successfully to '{new_name}' with price {new_price}.")
    
def show_restaurant_menu():
    print("Restaurant Menu:")
    items = MenuManager()
    items.all_items()
    
    

show_user_menu()
connection.close()