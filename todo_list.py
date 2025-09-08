from rich.console import Console
from rich.table import Table
import re
import time
console = Console()
import re
file_path = r"C:\Users\PC\Desktop\python_projects\todo.txt"
def add_task(task,completion_time):
    with open (file_path , "a") as f:
        f.write(f" {task} -  {completion_time}\n")
        print('adding task...')
        time.sleep(2)
        print("Task added successfully")
        time.sleep(2)
def view_tasks():
    with open (file_path , "r") as f:
        tasks = f.readlines()
        table = Table(title="To-Do List")
        table.add_column("Taks Number.", style="white", justify="left")
        table.add_column("Task", style="purple", justify="left")
        table.add_column("Deadline", style="red")
        for i, task in enumerate(tasks, start=1):
            name, deadline = task.strip().split(" - ")
            table.add_row(str(i), name, deadline)
        console.print(table)
def remove_task():
    while True:
        with open (file_path , "r") as f:
            while True:
                exit = False
                with open (file_path , "r") as f:
                    tasks = f.readlines()
                    print('*******remove tasks menu*********')
                    if len(tasks) == 0:
                        print("no tasks  available to remove")
                        print('exititng to main menu...')
                        time.sleep(2)
                        exit = True
                        break
                    print(f'there are {len(tasks)} tasks in the list')
                    view_tasks()
                    user_input = input('enter the task number you want to remove or press {{q}} to exit:')
                    if user_input.lower() == 'q':
                        print('exiting to main menu...')
                        time.sleep(2)
                        exit = True
                        break
                    elif user_input.isdigit():
                        if int(user_input) > len(tasks) or int(user_input) < 1:
                            print("invalid task number")
                            print('try again or press {{q}} to exit')
                            time.sleep(2)
                            continue
                        else:
                            task = int(user_input)
                            tasks.pop(task-1)
                            with open (file_path , "w") as f:
                                f.writelines(tasks)
                                print('removing task...')
                                time.sleep(2)
                                print("Task removed successfully")
                                print('Reloading menu...')
                                time.sleep(2)
                                exit = False
                                continue
                    else:
                        print("comeon you think we are here to waste our time?")
                        time.sleep(2)  
                        exit = True
                        break 
            if exit == True:
                break           
def complete_task():
    current_tasks = []
    with open (file_path, "r+") as f:
        tasks = f.readlines()
        while True:
            print('*******complete tasks menu*********')
            if len(tasks) == 0:
                print("no tasks available to complete")
                print('exiting to main menu...')
                time.sleep(2)
                break
            print(f'there are {len(tasks)} tasks in the list')
            view_tasks()
            user_input = input('enter the task number you want to complete or press {{q}} to exit:')
            if user_input.lower() == 'q':
                print('exiting to main menu...')
                time.sleep(2)
                break
            else:
                for task in enumerate(tasks):
                    current_tasks.append(task)
                    number = task[0]
                task_to_remove = int(user_input)
                for task in current_tasks:
                    if task[0] == (task_to_remove -1):
                        current_tasks.remove(task)
                        print(f'{task[1]} completed successfully')
                with open (file_path , "w") as f:
                    for task in current_tasks:
                        f.write(task[1])
                    print('completing...')
                    time.sleep(2)
                    print("Task completed and removed successfully")
                    print('Reloading menu...')
                    time.sleep(2)
                    continue
print('loading...')
time.sleep(2)
print("**********Welcome to the To-Do List App!**********")
while True:
    print("         1. Add Task")
    print("         2. View Tasks")
    print("         3. Remove Task")
    print("         4. Complete Task")
    print("         5. Exit")
    choice = input("Enter your choice: ")
    if choice == "1":
        print('loading...')
        time.sleep(2)
        print("**********Add Task Menu**********")
        while True:
            print('press {{q}} to exit')
            task = input("Enter the tasks: ")
            if task == "q":
                print('..........')
                time.sleep(2)
                break
            else:
                pass
            while True:
                days = {'monday','tuesday','wednesday','thursday','friday','saturday','sunday'}
                completion_day  = input("Enter the completion day: ")
                if completion_day.lower() in days:
                    break
                else:
                    print("Please enter a valid day")
            while True:
                re.compile(r"([01]?[0-9]|2[0-3]):[0-5][0-9]")
                completion_time = input("Enter the completion time (in 24-hour format)(hh:mm): ")
                if re.match(r"([01]?[0-9]|2[0-3]):[0-5][0-9]", completion_time):
                    break
                else:
                    print("Please enter a valid time")
            completion_time = (f'{completion_day} at {completion_time} hours')
            add_task(task,completion_time)
    elif choice == "2":
        print('loading...')
        time.sleep(2)
        print('**********view tasks menu************ ')
        view_tasks()
    elif choice == "3":
        print('loading...')
        time.sleep(2)   
        remove_task()
    elif choice == "4":
        print('loading...')
        time.sleep(2)
        complete_task()
    elif choice == "5":
        print("Goodbye!")
        print('exiting app ...')
        print('..........')
        time.sleep(2)
        break
    