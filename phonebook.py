from rich import print
from rich.console import Console
from rich.table import Table
console = Console()

def add_contact(name, phone_number):
    with open("phonebook.txt", "a") as f:
        f.write(f"{name},{phone_number}\n")
    print("Contact added successfully!")
def delete_contact(name):
    with open("phonebook.txt", "r") as f:
        lines = f.readlines()
    with open("phonebook.txt", "w") as f:
        for line in lines:
            if name not in line:
                f.write(line)
    print("Contact deleted successfully!")
def update_contact(name,phone_number):
    with open("phonebook.txt", "r") as f:
        lines = f.readlines()
    with open("phonebook.txt", "w") as f:
        for line in lines:
            if name in line:
                f.write(f"{name},{phone_number}\n")
            else:
                f.write(line)
    print("Contact updated successfully!")
def search_contact(name):
    with open("phonebook.txt", "r") as f:
        lines = f.readlines()
    for line in lines:
        if name in line:
            name, phone_number = line.strip().split(",")
            return name, phone_number
    return None
def view_phonebook():
    with open("phonebook.txt", "r") as f:
        lines = f.readlines()
    table = Table(title="Phonebook")
    table.add_column("Name")
    table.add_column("Phone Number")
    for line in lines:
        name, phone_number = line.strip().split(",")
        table.add_row(name, phone_number)
    console.print(table)
while True:
    print("Phonebook Management System")
    print("1. Add Contact")
    print("2. Delete Contact")
    print("3. Update Contact")
    print("4. Search Contact")
    print("5. View Phonebook")
    print('6. Exit')
    choice = input("Enter your choice: ")
    if choice == "1":
        name = input("Enter name: ")
        phone_number = input("Enter phone number: ")
        add_contact(name, phone_number)
    elif choice == "2":
        name = input("Enter name: ")
        delete_contact(name)
    elif choice == "3":
        name = input("Enter name: ")
        phone_number = input("Enter phone number: ")
        update_contact(name, phone_number)
    elif choice == "4":
        name = input("Enter name: ")
        if search_contact(name):
            print(f'contact found\n {search_contact(name)}')
        else:
            print("Contact not found.")
    
    elif choice == "5":    
        view_phonebook()
    else:
        print("Invalid choice. Please try again.")