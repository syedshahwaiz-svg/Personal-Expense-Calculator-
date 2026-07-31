#budget stores the target maximum spending limit set by the user.
budget = 0.0

# 'expenses' is a list that will store all expenses.
expenses = []


def set_budget():
    try:
        amount = float(input("\nEnter your total budget (PKR/$): "))

        # Input validation: Ensure the budget is a positive number.
        if amount <= 0:
            print("Budget must be greater than zero!")
        else:
            budget = amount
            # Format to 2 decimal places using 2 d.f
            print(f"Success: Budget set to {budget:.2f}")

    except ValueError:
        print("Invalid input! Please enter a valid numerical value.")


def add_expense():
    """Collect details for a new transaction and store it in the history list."""
    print("\n--- Add New Expense ---")

    category = input("Enter category (e.g., Food, Transport, Books, Utilities): ").strip().title()
    
    if not category or not category.replace(" ", "").isalpha():
        print("Invalid category! Category must contain only letters.")
        return

    description = input("Enter brief description: ").strip()
    
    if not description or not description.replace(" ", "").isalpha():
        print("Invalid description! Description must contain letters, not numbers.")
        return

    # 3. Validate Amount
    try:
        amount = float(input("Enter amount spent: "))

        if amount <= 0:
            print("Amount must be positive!")
            return

        expense_entry = {
            "category": category,
            "description": description,
            "amount": amount
        }

        expenses.append(expense_entry)
        print(f"Success: Added '{description}' ({amount:.2f}) under [{category}].")

    except ValueError:
        print("Invalid amount! Please enter a numeric value.")


def show_summary():
    print("\n================ SUMMARY REPORT ================")

    # Calculate total money spent by summing the amount of every expence in the list.
    total_spent = sum(item["amount"] for item in expenses)

    # Calculate remaining budget allowance.
    remaining = budget - total_spent

    print(f"Total Budget    : {budget:.2f}")
    print(f"Total Spent     : {total_spent:.2f}")
    print(f"Remaining Budget: {remaining:.2f}")

    # Conditional Warning System
    if budget > 0 and total_spent > budget:
        print("\n⚠️ WARNING: You have exceeded your set budget!")
    elif budget > 0 and remaining < (budget * 0.2):
        print("\n⚠️ NOTICE: You have spent over 80% of your budget!")

    # Calculate spending aggregated per category using a dictionary.
    category_totals = {}
    for item in expenses:
        cat = item["category"]
        
        category_totals[cat] = category_totals.get(cat, 0.0) + item["amount"]

    print("\nSpending Breakdown by Category:")
    if not category_totals:
        print("  No transactions recorded yet.")
    else:
        
        for cat, total in category_totals.items():
            print(f"  - {cat}: {total:.2f}")

    print("=================================================")


def view_all_expenses():
    """Display all recorded expenses sequentially line by line."""
    print("\n--- Transaction History ---")

    # Check if the list is empty before attempting to display transactions.
    if not expenses:
        print("No expenses recorded yet.")
        return
        
    for idx, item in enumerate(expenses, 1):
        print(f"{idx}. [{item['category']}] {item['description']} - {item['amount']:.2f}")


def main_menu():
    """Main execution loop that presents a interactive menu to the user."""
    # Infinite loop to keep app running until option 5 (Exit) is selected.
    while True:
        print("\n=========================================")
        print("     PERSONAL EXPENSE & BUDGET TRACKER   ")
        print("=========================================")
        print("1. Set / Update Budget")
        print("2. Add New Expense")
        print("3. View Summary Report")
        print("4. View All Transactions")
        print("5. Exit")

        # Prompt user to choose
        choice = input("\nSelect an option (1-5): ").strip()

       
        if choice == "1":
            set_budget()
        elif choice == "2":
            add_expense()
        elif choice == "3":
            show_summary()
        elif choice == "4":
            view_all_expenses()
        elif choice == "5":
            print("\nThank you for using Expense Tracker. Goodbye!")
            break  # Terminates the while loop to end the program
        else:
            print("Invalid selection! Please choose an option between 1 and 5.")



if __name__ == "__main__":
    main_menu()
