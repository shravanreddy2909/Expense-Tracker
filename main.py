import json
import os

expenses = {}
expense_history = []
total_expense = 0
if os.path.exists("expenses.json"):
    with open("expenses.json", "r") as file:
        expense_history = json.load(file)

    for expense in expense_history:
        category = expense["category"]
        amount = expense["amount"]

        if category in expenses:
            expenses[category] += amount
        else:
            expenses[category] = amount

        total_expense += amount
while True:
    try:
        budget = float(input("Enter your budget: "))

        if budget > 0:
            break

        print("Budget must be positive. Enter a valid budget.")

    except ValueError:
        print("Invalid input! Enter a valid number.")

while True:
    category = input("Enter the category: ").strip()

    while not category:
        print("Category cannot be empty!")
        category = input("Enter a valid category: ").strip()

    while True:
        try:
            amount = float(input("Enter amount: "))

            if amount > 0:
                break

            print("Amount must be positive. Enter a valid amount.")

        except ValueError:
            print("Invalid input! Enter a valid amount.")

    # Update category-wise expenses
    if category in expenses:
        expenses[category] += amount
    else:
        expenses[category] = amount

    # Store individual expense history
    expense_history.append({
        "category": category,
        "amount": amount
    })

    total_expense += amount

    # Budget warning
    if total_expense > budget:
        print("\nWARNING: You are crossing your budget!")
        print(f"Total expenditure: ₹{total_expense:.2f}")

    # Ask whether to add another expense
    while True:
        choice = input(
            "Do you want to add another expense? (yes/no): "
        ).strip().lower()

        if choice == "yes" or choice == "no":
            break

        print("Please enter yes or no.")

    if choice == "no":
        break

# Ask whether to display the summary
show_summary = input(
    "\nDo you want to view your expense summary? (yes/no): "
).strip().lower()

if show_summary == "yes":
    print("\n===== SMART EXPENSE ANALYZER =====")
    print(f"Your budget: ₹{budget:.2f}")

    for category, amount in expenses.items():
        print(f"{category}: ₹{amount:.2f}")

    print(f"Total expenditure: ₹{total_expense:.2f}")
    print(f"Remaining budget: ₹{budget - total_expense:.2f}")

    # Find the highest spending category using a for loop
    highest_category = ""
    highest_amount = 0

    for category, amount in expenses.items():
        if amount > highest_amount:
            highest_amount = amount
            highest_category = category

    print(f"Highest spending category: {highest_category}")
    print(f"Highest amount: ₹{highest_amount:.2f}")

    if total_expense > budget:
        print("Status: Budget exceeded!")
    else:
        print("Status: Within budget.")

    print("==================================")

# Ask whether to display expenditure history
show_history = input(
    "\nDo you want to view your expenditure history? (yes/no): "
).strip().lower()

if show_history == "yes":
    print("\n===== EXPENDITURE HISTORY =====")

    for expense in expense_history:
        print(
            f"Category: {expense['category']} | "
            f"Amount: ₹{expense['amount']:.2f}"
        )

    print("================================")
with open("expenses.json", "w") as file:
    json.dump(expense_history, file, indent=4)

print("Expenses saved successfully!")