import datetime
from rich import print
from rich.console import Console
from rich.table import Table   
import time
console = Console()
today = datetime.datetime.now().strftime("%Y-%m-%d")


def add_expense():
    expense_name = input("Enter the name of the expense: ")
    expense_amount = float(input("Enter the amount of the expense: "))
    expense_date = ''
    print("enter 1 to add today's date or 2 to enter a custom date")
    choice = input("Enter your choice: ")
    if choice == '1':
        expense_date = today
    elif choice == '2':
        
        print("Enter the date of the expense (YYYY-MM-DD): ")
        while True:
            try:
                expense_date = input()
                datetime.datetime.strptime(expense_date, "%Y-%m-%d")
                break
            except ValueError:
                print("Invalid date format. Please try again.")
    expense = {
        "name": expense_name,
        "amount": expense_amount,
        "date": expense_date
    }
    with open("expenses.txt", "a") as f:
        f.write(f"{expense_name},{expense_amount},{expense_date}\n")
    print("Expense added successfully!")

def view_expenses():
    with open("expenses.txt", "r") as f:
        expenses = f.readlines()
    table = Table(title="Expenses")
    table.add_column("Name")
    table.add_column("Amount")
    table.add_column("Date")
    for expense in expenses:
        name, amount, date = expense.strip().split(",")
        table.add_row(name, amount, date)
    table.add_row("[bold red]Total[/bold red]",  f'[bold red]{view_total_expenses()}[/bold red]',"")
    table.add_row("[bold yellow]Remaining Salary[/bold yellow]", f'[bold yellow]{remaining_salary()}[/bold yellow]',"")
    console.print(table)

def view_total_expenses():
    with open("expenses.txt", "r") as f:
        expenses = f.readlines()
    total = 0
    for expense in expenses:
        amount = float(expense.strip().split(",")[1])
        total += amount
    return total
print("Expense Management System")
print("Date:", today)
with open ("salary.txt", "r+") as f:
    salary = f.read()
    if not salary:
        salary = float(input("Enter your salary: "))
        f.write(str(salary))
        print("Salary set to", salary)

def remaining_salary():
    return float(salary) - view_total_expenses()

def check_salary_status():
    if view_total_expenses() == 0:
        print("\n[bold green]You have not spent any money yet.[/bold green]\n")
        print(f'[bold red]remaining salary:[/bold red] {remaining_salary()}\n')
    elif remaining_salary() < 0:
        print("\n[bold red]You are in debt now![/bold red]\n")
        print(f'[bold red]remaining salary:[/bold red] {remaining_salary()}\n')
    elif remaining_salary() < (float(salary) / 2):
        print("\n[bold yellow]Your remaining salary is less than half![/bold yellow]\n")
        print(f'[bold red]remaining salary:[/bold red] {remaining_salary()}\n')
    elif remaining_salary() < (float(salary) / 10):
        print("\n[bold blue]Your salary is almost gone![/bold blue]\n")
        print(f'[bold red]remaining salary:[/bold red] {remaining_salary()}\n')
    
        
while True:
    print("1. Add Expense")
    print("2. View Expenses")
    print("3. View Salary Status")
    print("4. Exit")
    choice = input("Enter your choice: ")
    if choice == "1":
        add_expense()
    elif choice == "2":
        view_expenses()
    elif choice == "3":
        check_salary_status()
    elif choice == "4":
        print("Goodbye!")
        print('exiting app ...')
        print('..........')
        time.sleep(2)
        break
    else:
        print("Invalid choice. Please try again.")