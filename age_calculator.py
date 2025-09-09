import datetime
import time
import re
from rich import print
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
def days_to_birthday(born):
    today = datetime.date.today()
    next_birthday = datetime.date(today.year, born.month, born.day)
    if next_birthday < today:
        next_birthday = datetime.date(today.year + 1, born.month, born.day)
    return (next_birthday - today).days
def print_options():
        print('how do you want to calculate your age')
        print('1. [bold blue underline]in seconds[bold blue underline]')
        print('2. [bold blue underline]in minutes[bold blue underline]')
        print('3. [bold blue underline]in hours[bold blue underline]')
        print('4. [bold blue underline]in days[bold blue underline]')
        print('5. [bold blue underline]in years[bold blue underline]')
        print('6. [bold blue underline]in all formats[bold blue underline]')
        print('7. [bold blue underline]days to your birthday[bold blue underline]')
        print('8. [bold red underline]exit[bold red underline]')
def calculattion(choice,birth_date):
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
        elif choice == 6:
            print(f'your age in seconds is {calculattion(1,birth_date)} seconds')
            print(f'your age in minutes is {calculattion(2,birth_date)} minutes')
            print(f'your age in hours is {calculattion(3,birth_date)} hours')
            print(f'your age in days is {calculattion(4,birth_date)} days')
            print(f'your age in years is {calculattion(5,birth_date)} years')
        elif choice == 7:
            print(f'days to your next  birthday is [bold red underline]{days_to_birthday(birth_date)}[/bold red underline] days away')
        elif choice == 8:
            return False
        else:
            print('please enter a valid choice')
def get_date_choice():
        while True:
            year = input('enter the year you were born\n')
            if re.match(r"^(202[0-5]|20[01][0-9]|1[0-9]{3}|[0-9]{1,3})$", year) :
                break
            else:
                print('please enter a valid year')
        while True:
            month = input('enter the month you were born (format in numbers)\n')
            if re.match(r'^(1[0-2]|[1-9])$', month) :
                break
            else:
                print('please enter a valid month')
        while True:
            day = input('enter the day you were born\n')
            if re.match(r'^([1-9]|1[0-9]|2[0-9]|3[0-1])$', day) :
                break
            else:
                print('please enter a valid day')
            # day = int(input('enter the day you were born\n'))
        birth_date = datetime.date(int(year), int(month), int(day))
        print('your date of birth is', birth_date)
        print_options()
        choice = int(input('enter your choice\n'))
        
        if choice > 0 and choice < 9:
                calculattion(choice,birth_date)
        else:
                print('please enter a valid choice')
        
    
print('**********welcome to age calculator**********')
print('getting today\'s day .....')
time.sleep(2)
print(f'today is {datetime.date.today()}')
get_date_choice()
# while True:
   
    
#     birth_date = datetime.date(int(year), int(month), int(day))
#     while True:
#         print_options()
#         choice = int(input('enter your choice\n'))
#         if choice == 1 or choice == 2 or choice == 3 or choice == 4 or choice == 5 or choice == 6 or choice == 7 or choice == 8:
            
#             break
#         else:
#             print('invalid choice')
    
    # print_options()
    # choice = int(input('enter your choice\n'))
   
    # if choice == 1:
    #     print('calsulating age in seconds...')
    #     time.sleep(2)
    #     print(f'your age in seconds is {age_in_seconds(birth_date)} seconds')
    #     while True:
    #         print('do you want to see in more formats')
    #         print_options()
    #         choice = int(input('enter your choice\n'))
    #         calculattion(choice)
            
    # elif choice == 2:
    #     print('calsulating age in minutes...')
    #     time.sleep(2)
    #     print(f'your age in minutes is {age_in_minutes(birth_date)} minutes')
    #     while True:
    #         print('do you want to see in more formats')
    #         print_options()
    #         choice = int(input('enter your choice\n'))
    #         calculattion(choice)
            
    # elif choice == 3:
    #     print('calsulating age in hours...')
    #     time.sleep(2)
    #     print(f'your age in hours is {age_in_hours(birth_date)} hours')
    #     while True:
    #         print('do you want to see in more formats')
    #         print_options()
    #         choice = int(input('enter your choice\n'))
    #         calculattion(choice)
            
    # elif choice == 4:
    #     print('calsulating age in days...')
    #     time.sleep(2)
    #     print(f'your age in days is {age_in_days(birth_date)} days')
    #     while True:
    #         print('do you want to see in more formats')
    #         print_options()
    #         choice = int(input('enter your choice\n'))
    #         calculattion(choice)
            
    # elif choice == 5:
    #     print('calsulating age in years...')
    #     time.sleep(2)
    #     print(f'your age in years is {age_in_years(birth_date)} years')
    #     while True:
    #         print('do you want to see in more formats')
    #         print_options()
    #         choice = int(input('enter your choice\n'))
    #         calculattion(choice)
            
    # elif choice == 6:
    #     print('calsulating age in all formats...')
    #     time.sleep(2)
    #     print(f'your age in seconds is {age_in_seconds(birth_date)} seconds')
    #     print(f'your age in minutes is {age_in_minutes(birth_date)} minutes')
    #     print(f'your age in hours is {age_in_hours(birth_date)} hours')
    #     print(f'your age in days is {age_in_days(birth_date)} days')
    #     print(f'your age in years is {age_in_years(birth_date)} years')
        
    # elif choice == 7:
    #     print('calsulating days to your birthday...')
    #     time.sleep(2)
    #     print(f'days to your next  birthday is [bold red underline]{days_to_birthday(birth_date)}[/bold red underline] days away')
    #     while True:
    #         print('do you want to calculate your age ?')
    #         print_options()
    #         choice = int(input('enter your choice\n'))
    #         calculattion(choice)
            
    # elif choice == 8:
    #     print('exiting app ...')
    #     print('..........')
    #     time.sleep(2)
    #     break
    # # elif   not calculattion(choice):
    # #     break
    # else:
    #     print('please enter a valid choice')

    # born = input("Enter your birth date (YYYY-MM-DD): ")
    # born = datetime.datetime.strptime(born, "%Y-%m-%d").date()
    # print("Your age in seconds is:", age_in_seconds(born))
    # print("Your age in minutes is:", age_in_minutes(born))
    # print("Your age in hours is:", age_in_hours(born))
    # print("Your age in days is:", age_in_days(born))
    # print("Your age in years is:", age_in_years(born))