from rich import print
import random
import re
import time
username = ''
with open("users.txt", "r") as f:
    line = f.readline()
    if line:
        for line in f:
            stored_user, stored_password, stored_email = line.strip().split("|")
            username = stored_user

def login():
    username = input("Enter your username: ")
    password = input("Enter your password: ")
    with open("users.txt", "r") as f:
        for line in f:
            user, stored_password, _ = line.strip().split("|")
            if user == username and password == stored_password:
                return True
    return False
def generate_password():
    characters = 'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789!@#$%&'
    password = ''.join(random.choice(characters) for _ in range(12))
    return password
def register():
    email = ''
    while True:
        temp = input("Enter your email: ")
        if re.match(r"^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-z]{2,}$", temp):
            email = temp
            break
        else:
            print("Invalid email format. Please try again.")

    username = ''
    print('1:to generate username\n2:to enter username manually')
    while True:
        choice = input('enter your choice\n')
        if choice  == '1':
            username = email.split('@')[0]
            print(f'your generated username is {username}')
        elif choice == '2':
            username = input('enter your username\n')
        else:
            print('invalid choice')
            continue
        break
    password = ''
    print('1:to generate password\n2:to enter password manually')
    while True:
        choice = input('enter your choice\n')
        if choice == '1':
            password = generate_password()
            print(f'your generated password is {password}\n dont show it to anyone ')
        elif choice == '2':
            password = input('enter your password\n')
        else:
            print('invalid choice')
            continue
        break
    with open("users.txt", "a") as f:
        f.write(f"{username}|{password}|{email}\n")
    print("Registration successful!")

def forgot_password():
    email = input("Enter your email: ")
    with open("users.txt", "r") as f:
        for line in f:
            stored_user, stored_password, stored_email = line.strip().split("|")
            user = stored_user
            stored_password = stored_password
            if email == stored_email:
                print('enter new password')
                print('1:to generate password\n2:to enter password manually')
                while True:
                    choice = input('enter your choice\n')
                    if choice == '1':
                        password = generate_password()
                    elif choice == '2':
                        password = input('enter your password\n')
                    else:
                        print('invalid choice')
                        continue
                    break
                print('enter new username')
                print('1:to generate username\n2:to enter username manually')
                while True:
                    choice = input('enter your choice\n')
                    if choice == '1':
                        username = email.split('@')[0]
                        print(f'your generated username is {username}')
                    elif choice == '2':
                        username = input('enter your username\n')
                    else:
                        print('invalid choice')
                        continue
                    break
                lines = f.readlines()
                with open("users.txt", "w") as f:
                    for line in lines:
                        user, stored_password, stored_email = line.strip().split("|")
                        f.write(f"{username}|{password}|{stored_email}\n")

                print("Password reset successful!")
                return True
    return False

def expense_management():
    global username
    import datetime
    from rich import print
    from rich.console import Console
    from rich.table import Table   
    import time
    console = Console()
    today = datetime.datetime.now().strftime("%Y-%m-%d")
    print(f'Welcome to the expense management system {username}')


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
print('1:login\n2:register\n3:forgot password\n4:exit app')
while True:
    choice = input('enter your choice\n')
    if choice == '1':
        if login():
            print('login successful')
            expense_management()
            break
        else:
            print('login failed')
            print('did you forget password ?\n1:yes\n2:no\n')
            choice = input('enter your choice\n')
            if choice == '1':
                if forgot_password():
                    break
                else:
                    continue
            else:
                continue
    elif choice == '2':
        register()
        if login():
            print('login successful')
            expense_management()
            break
        else:
            print('login failed')
    elif choice == '3':
        if forgot_password():
            break
        else:
            print('forgot password failed')
    elif choice == '4':
        print('exiting app ...')
        print('..........')
        time.sleep(2)
        break
    else:
        print('invalid choice')
        continue