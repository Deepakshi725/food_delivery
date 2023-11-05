#for user:
import json
class User:
    def __init__(self, full_name, phone_number, email, address, password):
        self.full_name = full_name
        self.phone_number = phone_number
        self.email = email
        self.address = address
        self.password = password
        self.orders = []

class FoodItem:
    def __init__(self, name, description, price):
        self.name = name
        self.description = description
        self.price = price

class Restaurant:
    def __init__(self):
        self.food_menu = {
            1: FoodItem("Tandoori Chicken", "4 pieces", 240),
            2: FoodItem("Vegan Burger", "1 Piece", 320),
            3: FoodItem("Truffle Cake", "500gm", 900)
        }

def register_user():
    full_name = input("Enter Full Name: ")
    phone_number = input("Enter Phone Number: ")
    email = input("Enter Email: ")
    address = input("Enter Address: ")
    password = input("Enter Password: ")
    user = User(full_name, phone_number, email, address, password)
    return user


def login_user(users, email, password):
    for user in users:
        if user.email == email and user.password == password:
            return user
    return None

def display_food_menu(restaurant):
    print("Food Menu:")
    for food_id, food_item in restaurant.food_menu.items():
        print(f"{food_id}. {food_item.name} ({food_item.description}) [INR {food_item.price}]")

def place_order(restaurant, user):
    display_food_menu(restaurant)
    selected_items = input("Enter the item numbers you want to order (e.g., 1 2 3): ").split()
    selected_items = [int(item) for item in selected_items]
    order_items = [restaurant.food_menu[item] for item in selected_items]
    user.orders.append(order_items)

def view_order_history(user):
    print("Order History:")
    for i, order in enumerate(user.orders, 1):
        print(f"Order {i}:")
        for item in order:
            print(f"{item.name} ({item.description}) [INR {item.price}]")
        print()

def update_profile(user):
    full_name = input("Enter Full Name: ")
    phone_number = input("Enter Phone Number: ")
    address = input("Enter Address: ")
    password = input("Enter New Password: ")
    user.full_name = full_name
    user.phone_number = phone_number
    user.address = address
    user.password = password

def main():
    users = []
    restaurant = Restaurant()

    while True:
        print("\nMenu Options:")
        print("1. Register")
        print("2. Login")
        print("3. Exit")

        choice = input("Enter your choice: ")

        if choice == '1':
            user = register_user()
            users.append(user)
            print("Registration successful.")

        elif choice == '2':
            email = input("Enter Email: ")
            password = input("Enter Password: ")
            logged_in_user = login_user(users, email, password)
            if logged_in_user:
                while True:
                    print("\nUser Options:")
                    print("1. Place New Order")
                    print("2. Order History")
                    print("3. Update Profile")
                    print("4. Logout")

                    user_choice = input("Enter your choice: ")

                    if user_choice == '1':
                        place_order(restaurant, logged_in_user)

                    elif user_choice == '2':
                        view_order_history(logged_in_user)

                    elif user_choice == '3':
                        update_profile(logged_in_user)
                        print("Profile updated successfully.")

                    elif user_choice == '4':
                        print("Logged out.")
                        break

        elif choice == '3':
            print("Goodbye!")
            break

if __name__ == "__main__":
    main()
