import datetime
import time
import re
def calculate_age(born):
    today = datetime.date.today()
    return today.year - born.year - ((today.month, today.day) < (born.month, born.day))
def age_in_seconds(born):
    today = datetime.date.today()
    return (today - born).total_seconds()
def age_in_minutes(born):
    today = datetime.date.today()
    return (today - born).total_seconds() / 60
def age_in_hours(born):
    today = datetime.date.today()
    return (today - born).total_seconds() / 60 / 60
def age_in_days(born):
    today = datetime.date.today()
    return (today - born).total_seconds() / 60 / 60 / 24
def age_in_years(born):
    today = datetime.date.today()
    return (today - born).total_seconds() / 60 / 60 / 24 / 365
print('**********welcome to age calculator**********')
print('getting today\'s day .....')
time.sleep(2)
print(f'today is {datetime.date.today()}')
while True:
    while True:
        year = input('enter the year you were born\n')
        if re.match(r"^(202[0-5]|20[01][0-9]|1[0-9]{3}|[0-9]{1,3})$", year) :
            break
        else:
            print('please enter a valid year')
    while True:
        month = input('enter the month you were born (format in numbers)\n')
        if re.match(r'^([0-9]|1[0-2]$)', month) :
            break
        else:
            print('please enter a valid month')
    while True:
        day = input('enter the day you were born\n')
        if re.match(r'^([0-9]|1[0-9]|2[0-9]|3[0-1]$)', day) :
            break
        else:
            print('please enter a valid day')
        # day = int(input('enter the day you were born\n'))
    birth_date = datetime.date(int(year), int(month), int(day))
    def print_options():
        print('how do you want to calculate your age')
        print('1. in seconds')
        print('2. in minutes')
        print('3. in hours')
        print('4. in days')
        print('5. in years')
    def calculattion(choice):
        if choice == 1:
            print(f'your age in seconds is {age_in_seconds(birth_date)}')
        elif choice == 2:
            print(f'your age in minutes is {age_in_minutes(birth_date)}')
        elif choice == 3:
            print(f'your age in hours is {age_in_hours(birth_date)}')
        elif choice == 4:
            print(f'your age in days is {age_in_days(birth_date)}')
        elif choice == 5:
            print(f'your age in years is {age_in_years(birth_date)}')
        else:
            print('please enter a valid choice')
    print_options()
    choice = int(input('enter your choice\n'))
    if choice == 1:
        print('calsulating age in seconds...')
        time.sleep(2)
        print(f'your age in seconds is {age_in_seconds(birth_date)}')
        print('do you want to see in more formats')
        print_options()
        choice = int(input('enter your choice\n'))
        calculattion(choice)
    elif choice == 2:
        print('calsulating age in minutes...')
        time.sleep(2)
        print(f'your age in minutes is {age_in_minutes(birth_date)}')
        print('do you want to see in more formats')
        print_options()
        choice = int(input('enter your choice\n'))
        calculattion(choice)
    elif choice == 3:
        print('calsulating age in hours...')
        time.sleep(2)
        print(f'your age in hours is {age_in_hours(birth_date)}')
        print('do you want to see in more formats')
        print_options()
        choice = int(input('enter your choice\n'))
        calculattion(choice)
    elif choice == 4:
        print('calsulating age in days...')
        time.sleep(2)
        print(f'your age in days is {age_in_days(birth_date)}')
        print('do you want to see in more formats')
        print_options()
        choice = int(input('enter your choice\n'))
        calculattion(choice)
    elif choice == 5:
        print('calsulating age in years...')
        time.sleep(2)
        print(f'your age in years is {age_in_years(birth_date)}')
        print('do you want to see in more formats')
        print_options()
        choice = int(input('enter your choice\n'))
        calculattion(choice)
    else:
        print('please enter a valid choice')

    # born = input("Enter your birth date (YYYY-MM-DD): ")
    # born = datetime.datetime.strptime(born, "%Y-%m-%d").date()
    # print("Your age in seconds is:", age_in_seconds(born))
    # print("Your age in minutes is:", age_in_minutes(born))
    # print("Your age in hours is:", age_in_hours(born))
    # print("Your age in days is:", age_in_days(born))
    # print("Your age in years is:", age_in_years(born))