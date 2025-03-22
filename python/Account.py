# Importing Libraries

import datetime

# Initializing class to hold expenses and income
class Account:
    
    def __init__(self):
    # Create list of transactions to store income and expenses
        self.transactions = []


    # Function to log expenses
    def log_expense(self, date, amount, category, description=""):
        ## Error checking to make sure date it in the correct format.
        try:
            date = datetime.datetime.strptime(date, "%Y-%m-%d").date()
            self.transactions.append(
                {
                    "date": date,
                    "type": "expense",
                    "amount": amount,
                    "category": category,
                    "description": description
                })
            return True
        except ValueError:
            print("Incorrect date format, use YYYY-MM-DD")
            return False
        
    # Function to log income
    def log_income(self, date, amount, description=""):
     # Error checking date format.
        try:
            date = datetime.datetime.strptime(date, "%Y-%m-%d").date()
            self.transactions.append(
                {
                    "date": date,
                    "type": "income",
                    "amount": amount,
                    "description": description
                })
            return True
        except ValueError:
            print("Incorrect date format, use YYYY-MM-DD")
            return False          

    # Function to filter expenses by start date, end date, category, maximum amount and minimum amount
    def filter_expenses(self, start_date=None, end_date=None, category=None, amount_min=None, amount_max=None): 
        # Creating list for filtered expenses
        filter_expenses = []
        for transaction in self.transactions:
            ## Only filter expenses excluding income type.
            if transaction["type"] == "expense":    
            # Filter by Dates
                if start_date and transaction["date"] < datetime.datetime.strptime(start_date, "%Y-%m-%d").date():
                    continue
                if end_date and transaction["date"] < datetime.datetime.strptime(end_date, "%Y-%m-%d").date():
                    continue
            # Filter by Category
                if category and transaction.get("category", "").lower() != category.lower():
                    continue
            # Filter by Amount
                if amount_max and transaction["amount"] > amount_max:
                    continue
                if amount_min and transaction["amount"] < amount_min:
                    continue
                filter_expenses.append(transaction)
            return filter_expenses    

        
    # Function to display a list of all expenses.
    def show_all_expenses(self):
        # TO DO

    #Function to display all income. 
    def show_all_income(self):
        # TO DO
    
    # Function to display income/expense money movement. 
    def show_money_movements(self):
        # TO DO

## User Prompt and Selections

# Prompt the user for input.
def get_input(prompt, data_type=str):
    # Error Checking to ensure input is valid.
    while True:
        try:
            return data_type(input(prompt))
        except ValueError:
            print(f"Invalid input, Please enter valid {data_type.__name__}.")

# Showing Selectin options
if __name__ == "__main__":
    account = Account()

    while True:
        print("\nSelection Options:")
        print("1. Log Income")
        print("2. Log Expense")
        print("3. Filter Expenses")
        print("4. Show All Income")
        print("5. Show All Expenses")
        print("6. Show Money Movement (Income/Expense)")
        print("7. Exit")

        selection = get_input("Enter your selection (Numeric value): ", int)

        # Selection choice, Log Income
        if selection == 1:
            date = get_input("Enter income date (YYYY-MM-DD): ")
            amount = get_input("Enter income amount: ", float)
            description = get_input("Enter income description (Optional): ")
            if account.log_income(date, amount, description):
                print("Income logged.")
        
        # Selection choice, Log Expense
        elif selection == 2:
            date = get_input("Enter expense date (YYYY-MM-DD): ")
            amount = get_input("Enter expense amount: ", float)
            category = get_input("Enter expense category: ")
            description = get_input("Enter expense description (Optional): ")
            if account.log_expense(date, amount, category, description):
                print("Expense logged.")
        
        # Selection choice, Filter Expenses
        elif selection == 3:
            start_date = input("(Optional) Enter start date (YYYY-MM-DD): ") or None
            end_date = input("(Optional) Enter end date (YYYY-MM-DD): ") or None
            category = input("(Optional) Enter category: ") or None
            amount_max = get_input("(Optional) Enter maximum amount: ", float) if input("Optional) Enter maximum amount: ") else None
            amount_min = get_input("(Optional) Enter minimum amount: ", float) if input("Optional) Enter minimum amount: ") else None
            filter_expenses = account.filter_expenses(start_date, end_date, category, amount_max, amount_min)
            if filter_expenses:
                print("\nFiltered Expenses:")
                # Show expense(s) based on filter.
                for expense in filter_expenses:
                    print(f"Date: {expense['date'].strftime('%Y-%m-%d')}, Amount: ${expense['amount']:.2f}, Category: {expense['category']}, Description: {expense['description']}")

        # Selection choice, Display All Income
        elif selection == 4:
            account.show_all_income()

        # Selection choice, Display All Expense
        elif selection == 5:
            account.show_all_expenses()

        # Selection choice, Display Money Movement
        elif selection == 6:
            account.show_money_movement()

        # Selection choice, Exit Application
        elif selection == 7:
            print("Exiting Application...")
            break
        
        else:
            print("Invalid selection, try again.")
