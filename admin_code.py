#for admin:
class FoodMenu:
    def __init__(self):
        self.menu = {}
        self.food_id_counter = 1

    def add_food_item(self, name, quantity, price, discount, stock):
        food_id = self.food_id_counter
        self.menu[food_id] = {
            "Name": name,
            "Quantity": quantity,
            "Price": price,
            "Discount": float(discount),
            "Stock": stock
        }
        self.food_id_counter += 1
        return food_id

    def edit_food_item(self, food_id, name, quantity, price, discount, stock):
        if food_id in self.menu:
            self.menu[food_id] = {
                "Name": name,
                "Quantity": quantity,
                "Price": price,
                "Discount": float(discount),
                "Stock": stock
            }
            return True
        return False

    def view_food_items(self):
        return self.menu

    def remove_food_item(self, food_id):
        if food_id in self.menu:
            del self.menu[food_id]
            return True
        return False

def main():
    food_menu = FoodMenu()
    
    while True:
        print("\nMenu Options:")
        print("1. Add new food item")
        print("2. Edit food item")
        print("3. View food items")
        print("4. Remove food item")
        print("5. Exit")

        choice = input("Enter your choice: ")

        if choice == '1':
            name = input("Enter food item name: ")
            quantity = input("Enter quantity: ")
            price = float(input("Enter price: "))
            discount = float(input("Enter discount: "))
            stock = int(input("Enter stock amount: "))
            food_id = food_menu.add_food_item(name, quantity, price, discount, stock)
            print(f"Food item added with ID: {food_id}")

        elif choice == '2':
            food_id = int(input("Enter Food ID to edit: "))
            name = input("Enter updated food item name: ")
            quantity = input("Enter updated quantity: ")
            price = float(input("Enter updated price: "))
            discount = float(input("Enter updated discount: "))
            stock = int(input("Enter updated stock amount: "))
            if food_menu.edit_food_item(food_id, name, quantity, price, discount, stock):
                print("Food item updated successfully.")
            else:
                print("Food item not found.")

        elif choice == '3':
            menu = food_menu.view_food_items()
            for food_id, details in menu.items():
                print(f"Food ID: {food_id}")
                for key, value in details.items():
                    print(f"{key}: {value}")
                print()

        elif choice == '4':
            food_id = int(input("Enter Food ID to remove: "))
            if food_menu.remove_food_item(food_id):
                print("Food item removed successfully.")
            else:
                print("Food item not found.")

        elif choice == '5':
            print("Goodbye!")
            break

        else:
            print("Invalid choice. Please enter a valid option.")

if __name__ == "__main__":
    main()