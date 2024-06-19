                                            #SMART EXPENSE TRACKER WITH DATA VISULIZATION

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

expenses = {}               #Initializes the expense data dictionary

def add_expense():
    while True:
        print(" ")
        print("Select a category:")
        print("1. Travel")
        print("2. Food")
        print("3. Entertainment")
        print("4. Shopping")
        print("5. Other (manual entry)")
        category_choice = input("Enter choice: ")
        if category_choice == "1":
            category = "Travel"
            break
        elif category_choice == "2":
            category = "Food"
            break
        elif category_choice == "3":
            category = "Entertainment"
            break
        elif category_choice == "4":
            category = "Shopping"
            break
        elif category_choice == "5":
            category = input("Enter custom category: ")
            break
        else:
            print("Invalid choice. Please try again.")
    while True:
        try:
            amount = float(input("Enter expense amount: "))
            if amount <= 0:
                print("Amount must be a positive number. Please try again.")
                continue
            if category in expenses:
                expenses[category] += amount              #Adds the new amount to the existing amount  
            else:
                expenses[category] = amount
            save_expenses() 
            print("Expense added successfully!")
            break
        except ValueError:
            print("Invalid amount. Please enter a valid number.")


def view_expenses():
    if len(expenses) == 0:
        print("No expenses to display.")
    else:
        print(" ")
        print("*" * 167)
        print(" "*75 + "Expenses" + " "*75)
        print("*" * 167)
        print(" ")
        for category, amount in expenses.items():
            print(f"{category}: Rs.{amount:.2f}")
        


def filter_expenses():
    category = input("Enter category to filter: ")
    filtered_expenses = {k: v for k, v in expenses.items() if k == category}
    if not filtered_expenses:
        print("No expenses found for this category.")
    else:
        print(" ")
        print(f"Expenses for {category}:")
        for k, v in filtered_expenses.items():
            print(f" Rs.{v:.2f}")


def edit_expenses():
    while True:
        category = input("Enter category to edit: ")
        if category not in expenses:
            print("Category not found. Please try again.")
            continue
        try:
            amount = float(input("Enter new amount: "))
            if amount <= 0:
                print("Amount must be a positive number. Please try again.")
                continue
            expenses[category] = amount
            save_expenses()  
            print("Expense edited successfully!")
            break
        except ValueError:
            print("Invalid amount. Please enter a valid number.")


def remove_expenses():
    category = input("Enter category to remove: ")
    if category not in expenses:
        print("Category not found. Please try again.")
    else:
        del expenses[category]
        save_expenses()  
        print("Expense removed successfully!")


def save_expenses():
    try:
        with open("expenses.txt", "a") as f:            #Using "a" to append instead of "w" to avoid overwriting of the amount
            for category, amount in expenses.items():
                f.write(f" {category}: Rs.{amount}\n")
    except IOError as e:
        print(f"Error saving expenses: {e}")


def load_expenses():
    global expenses
    expenses = {}                                        #Clears expenses to avoid duplicates
    try:
        with open("expenses.txt", "r") as f:
            for line in f:
                category, amount = line.strip().split(":")
                if category in expenses:
                    expenses[category] += float(amount)  #Adds the amount to the existing category if present
                else:
                    expenses[category] = float(amount)   #Else adds the amount to the respective category
    except FileNotFoundError:
        pass
    except IOError as e:
        print(f"Error loading expenses: {e}")


def visualize_expenses():
    if not expenses:
        print("No expenses to visualize.")
    else:
        df = pd.DataFrame(list(expenses.items()), columns=['Category', 'Amount'])
        print("Choose a visualization option:")
        print("1. Bar Plot")
        print("2. Pie Chart")
        choice = input("Enter choice: ")

         #BAR PLOT
        if choice == "1":
            plt.bar(df['Category'], df['Amount'])
            plt.xlabel("Category")
            plt.ylabel("Amount")
            plt.title("Expenses")
            plt.show()

        #PIE CHART    
        elif choice == "2":
            plt.pie(df['Amount'], labels=df['Category'],autopct='%1.1f%%')
            plt.title("Expenses")
            plt.tight_layout() 
            plt.show()
            
        else:
            print("Invalid choice. Please try again.")

#Main program
load_expenses()
print(" ")
print(" ")
print(" "*30 + "-" * 106)
print(" "*30 + "|" + " "*104 + "|")
print(" "*30 + "|" + " " * 104 + "|")
print(" "*30 + "|" + " " * 30 + "SMART EXPENSE TRACKER WITH DATA VISUALIZATION" + " " * 29 + "|")
print(" "*30 + "|" + " "*104 + "|")
print(" "*30 + "|" + " "*104 + "|")
print(" "*30 + "|" + " " * 74 + "BY:- " + " " * 25 + "|")
print(" "*30 + "|" + " " * 78 + "TANISHA SHAHA" + " " * 13 + "|")
print(" "*30 + "|" + " " * 104 + "|")
print(" "*30 + "-" * 106)
print(" ")
print(" ")

while True:
    print(" ")
    print("*" * 167)
    print(" "*75 + "Main Menu" + " "*75)
    print("*" * 167)
    print(" ")
    print("1. Add new expense")
    print("2. View all expenses")
    print("3. Filter expenses by category")
    print("4. Edit expense")
    print("5. Remove expense")
    print("6. Visualize expenses")
    print("7. Quit")
    choice = input("Enter choice: ")
    if choice == "1":
        add_expense()
    elif choice == "2":
        view_expenses()
    elif choice == "3":
        filter_expenses()
    elif choice == "4":
        edit_expenses()
    elif choice == "5":
        remove_expenses()
    elif choice == "6":
        visualize_expenses()
    elif choice == "7":
        break
    else:
        print("Invalid choice. Please try again.")