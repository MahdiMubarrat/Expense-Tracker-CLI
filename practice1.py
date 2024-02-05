import json

def main_menu():
    while True:
        print("\n1. Sign Up 2. Log In 3. Exit")
        choice = input("Enter choice: ")
        if choice == "1":
            sign_up()
        elif choice == "2":
            username = input("Enter username: ")
            if log_in(username):
                user_dashboard(username)
        elif choice == "3":
            break

def sign_up():
    username = input("Username: ")
    password = input("Password: ")
    data = {"password": password, "transactions": [], "budget": {}}
    with open(f"{username}.json", "w") as file:
        json.dump(data, file)
    print("Registered.")

def log_in(username):
    try:
        with open(f"{username}.json", "r") as file:
            data = json.load(file)
        return input("Password: ") == data["password"]
    except FileNotFoundError:
        print("User not found.")
        return False

def user_dashboard(username):
    while True:
        print("\n1. Add 2. Edit 3. Delete 4. View 5. Budget 6. Logout")
        choice = input("Enter choice: ")
        if choice == "1":
            add_transaction(username)
        elif choice == "2":
            edit_transaction(username)
        elif choice == "3":
            delete_transaction(username)
        elif choice == "4":
            view_transactions(username)
        elif choice == "5":
            set_budget(username)
        elif choice == "6":
            break

def add_transaction(username):
    transaction = {
        "type": input("Type (income/expense): "),
        "amount": float(input("Amount: ")),
        "category": input("Category: ")
    }
    save_transaction(username, transaction)

def save_transaction(username, transaction):
    data = load_data(username)
    data["transactions"].append(transaction)
    save_data(username, data)

def edit_transaction(username):
    view_transactions(username)
    index = int(input("Index to edit: ")) - 1
    data = load_data(username)
    if 0 <= index < len(data["transactions"]):
        data["transactions"].pop(index)
        new_transaction = {
            "type": input("Type (income/expense): "),
            "amount": float(input("Amount: ")),
            "category": input("Category: ")
        }
        data["transactions"].insert(index, new_transaction)
        save_data(username, data)

def delete_transaction(username):
    view_transactions(username)
    index = int(input("Index to delete: ")) - 1
    data = load_data(username)
    if 0 <= index < len(data["transactions"]):
        data["transactions"].pop(index)
        save_data(username, data)

def view_transactions(username):
    print("\nTransactions:")
    data = load_data(username)
    for index, transaction in enumerate(data["transactions"], start=1):
        print(f"{index}. {transaction['type']} - {transaction['amount']} - {transaction['category']}")

def set_budget(username):
    category = input("Category: ")
    amount = float(input("Budget: "))
    data = load_data(username)
    data["budget"][category] = amount
    save_data(username, data)

def load_data(username):
    with open(f"{username}.json") as file:
        return json.load(file)

def save_data(username, data):
    with open(f"{username}.json", "w") as file:
        json.dump(data, file)

if __name__ == "__main__":
    main_menu()
