import re
file_path = "todo.txt"
def add_task(task,completion_time):
    with open (file_path , "a") as f:
        f.write(f"task name {{{task}}} - competion time {{{completion_time}}}\n") #f.write(task," - ",completion_time + "\n")
        print("Task added successfully")
def view_tasks():
    with open (file_path , "r") as f:
        tasks = f.readlines()
        print("Tasks Available:")
        for task in enumerate(tasks):
            number = task[0]
            print(number+1,':',task[1],end='\n')
def remove_task():
    view_tasks()
    task = int(input("Enter the task number to remove: "))
    with open (file_path , "r") as f:
        tasks = f.readlines()
        tasks.pop(task-1)
        with open (file_path , "w") as f:
            f.writelines(tasks)
            print("Task removed successfully")
def complete_task():
    current_tasks = []
    with open (file_path, "r+") as f:
        tasks = f.readlines()
        print(f'there are {len(tasks)} tasks in the list')
        #print(tasks)
        #current_tasks = []
        for task in enumerate(tasks):
            current_tasks.append(task)
            #print(current_tasks)
            number = task[0]
            #print(type(number))
            print(number+1,':',task[1],end='')
    print('select the task you want to complete\n')
    task_to_remove = int(input('enter the task number\n'))
    for task in current_tasks:
        if task[0] == (task_to_remove -1):
            current_tasks.remove(task)
            print(f'{task[1]} completed successfully')
            break
    #print(current_tasks)
    with open (file_path , "w") as f:
        for task in current_tasks:
            f.write(task[1])
        print("Task completed and removed successfully")
while True:
    print("1. Add Task")
    print("2. View Tasks")
    print("3. Remove Task")
    print("4. Complete Task")
    print("5. Exit")
    choice = input("Enter your choice: ")
    if choice == "1":
        while True:
            print('press {{q}} to exit')
            task = input("Enter the tasks: ")
            
            if task == "q":
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
        view_tasks()
    elif choice == "3":
        remove_task()
    elif choice == "4":
        complete_task()
    elif choice == "5":
        break
    