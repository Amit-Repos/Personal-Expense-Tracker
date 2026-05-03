import csv
import os

expenses = []
BUDGET_FILE = "budget.txt"
CSV_FILE = "expenses.csv"

def add_expense():
    date = input("Enter date (YYYY-MM-DD): ")
    category = input("Enter category: ")
    amount = float(input("Enter amount: "))
    description = input("Enter description: ")

    expense = {
        "date": date,
        "category": category,
        "amount": amount,
        "description": description
    }
    expenses.append(expense)
    print("Expense added successfully!\n")


def view_expenses():
    if not expenses:
        print("No expenses found.\n")
        return

    for exp in expenses:
        if all(k in exp for k in ("date", "category", "amount", "description")):
            print(f"{exp['date']} | {exp['category']} | {exp['amount']} | {exp['description']}")
    print()


def set_budget():
    budget = float(input("Enter monthly budget: "))
    with open(BUDGET_FILE, "w") as f:
        f.write(str(budget))
    print("Budget saved!\n")


def track_budget():
    if not os.path.exists(BUDGET_FILE):
        print("No budget set.\n")
        return

    with open(BUDGET_FILE, "r") as f:
        budget = float(f.read())

    total = sum(exp["amount"] for exp in expenses)

    print(f"Total spent: {total}")
    if total > budget:
        print("You have exceeded your budget!\n")
    else:
        print(f"Remaining budget: {budget - total}\n")


def save_expenses():
    with open(CSV_FILE, "w", newline="") as f:
        writer = csv.DictWriter(f, fieldnames=["date", "category", "amount", "description"])
        writer.writeheader()
        writer.writerows(expenses)
    print("Expenses saved!\n")


def load_expenses():
    if os.path.exists(CSV_FILE):
        with open(CSV_FILE, "r") as f:
            reader = csv.DictReader(f)
            for row in reader:
                row["amount"] = float(row["amount"])
                expenses.append(row)


def menu():
    load_expenses()
    while True:
        print("1. Add Expense")
        print("2. View Expenses")
        print("3. Set Budget")
        print("4. Track Budget")
        print("5. Save & Exit")

        choice = input("Choose option: ")

        if choice == "1":
            add_expense()
        elif choice == "2":
            view_expenses()
        elif choice == "3":
            set_budget()
        elif choice == "4":
            track_budget()
        elif choice == "5":
            save_expenses()
            print("Goodbye!")
            break
        else:
            print("Invalid choice\n")


if __name__ == "__main__":
    menu()
