import json

expenses = []
categories = [
            "Food",
            "Travel",
            "Shopping",
            "Entertainment",
            "Study",
            "Other"
        ]
budget_limit = 0
budget_limit = int(input("Enter your monthly budget: "))
print("Your expense budget: ", budget_limit)

#save function 
def save_expenses(): #reuseable saving logic

    with open("expenses.json", "w") as file: #opens a file called expenses using writer mode

        json.dump(expenses, file) #take expense list convert to json file and then save into file 

#to load the file
def load_expenses():

    global expenses #Use the MAIN expenses variable from whole program

    try: #Try running this code. as opening can fail

        with open("expenses.json", "r") as file: #open the file and read it out

            expenses = json.load(file) #reads file and converts it to json text to python data

    except FileNotFoundError:

        expenses = []


load_expenses() #Load old data BEFORE app starts running
while True:

    print("\n=== EXPENSE TRACKER ===")
    print("1. Add Expense")
    print("2. View Expenses")
    print("3. Show Total Spending")
    print("4. Category wise Spending")
    print("5. Delete Expense")
    print("6. Exit")

    choice = input("Enter choice: ")

    if choice == "1":
        print("\nChoose Category:")

        for i, category in enumerate(categories, start=1):
            print(f"{i}. {category}")

        new_exp = int(input("Enter Category Number: "))
        if 1 <= new_exp <= len(categories):
            selected_category = categories[new_exp - 1]
            if selected_category == "Other":
                selected_category = input("Enter custom category: ")
            new_amt = int(input("Enter Amount: "))
            expenses_data = {
                "category" : selected_category,
                "amount" : new_amt
            }
            expenses.append(expenses_data)
            save_expenses()
            print("Expense added!")
        else:
            print("Invalid Option")

    elif choice == "2":
        if len(expenses)== 0:
            print("No expsense present")
        else:
            for i,exp in enumerate(expenses,start=1) :
                print(f"{i}. {exp['category']} - ₹{exp['amount']}")
    
    elif choice == "3":
        total = 0
        for exp in expenses:
            total = total + exp['amount']
        print("Total Spending: ",total)
        if total > budget_limit:
            print("You exceeded your budget!")

        elif total >= 0.8 * budget_limit:
            print("Warning: Near budget limit!")

        else:
            print("You are within budget.")
    

    elif choice == "4":
        category_totals = {}
        for exp in expenses:
            category = exp["category"]
            amount = exp["amount"]
            if category in category_totals:
                category_totals[category] += amount
            else:
                category_totals[category] = amount
        for category, total in category_totals.items():
            print(f"{category}: ₹{total}")


    elif choice == "5":
        exp_no = int(input("Enter expense number to delete: "))
        expenses.pop(exp_no - 1)

        print("Expense deleted!")

    elif choice == "6":
        print("Exit")
        break

    else:
        print("Invalid option!")