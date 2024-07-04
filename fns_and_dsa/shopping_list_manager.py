# shopping_list_manager.py

def display_menu():
    print("\n===== Shopping List Manager =====")
    print("1. Add item")
    print("2. Remove item")
    print("3. View list")
    print("4. Exit")

def main():
    shopping_list = []

    print("Shopping List Manager")  # Added as per the requirement

    while True:
        display_menu()

        choice = input("Enter your choice (1-4): ")

        if choice == '1':
            item = input("Enter item to add: ")
            shopping_list.append(item)
            print(f"'{item}' added to the shopping list.")

        elif choice == '2':
            if not shopping_list:
                print("Shopping list is empty.")
            else:
                item = input("Enter item to remove: ")
                if item in shopping_list:
                    shopping_list.remove(item)
                    print(f"'{item}' removed from the shopping list.")
                else:
                    print(f"'{item}' not found in the shopping list.")

        elif choice == '3':
            if not shopping_list:
                print("Shopping list is empty.")
            else:
                print("=== Shopping List ===")
                for index, item in enumerate(shopping_list, start=1):
                    print(f"{index}. {item}")

        elif choice == '4':
            print("Exiting...")
            break

        else:
            print("Invalid choice. Please enter a number from 1 to 4.")

if __name__ == "__main__":
    main()

