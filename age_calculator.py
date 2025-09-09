import datetime
import time
import re
from rich import print
from rich.console import Console
from rich.table import Table
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
def age_in_months(born):
    today = datetime.date.today()
    return (today.year - born.year) * 12 + (today.month - born.month)
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
        print('     1.[underline white ]............[/underline white] [bold blue underline]in seconds[bold blue underline]')
        print('     2.[underline white ]............[/underline white] [bold blue underline]in minutes[bold blue underline]')
        print('     3.[underline white ]............[/underline white] [bold blue underline]in hours[bold blue underline]')
        print('     4.[underline white ]............[/underline white] [bold blue underline]in days[bold blue underline]')
        print('     5.[underline white ]............[/underline white] [bold blue underline]in months[bold blue underline]')
        print('     6.[underline white ]............[/underline white] [bold blue underline]in all years[bold blue underline]')
        print('     7.[underline white ]............[/underline white] [bold blue underline]in all formats[bold blue underline]')
        print('     8.[underline white ]............[/underline white] [bold blue underline]days to your birthday[bold blue underline]')
        print('     9.[underline white ]............[/underline white] [bold red underline]exit[bold red underline]')
def calculattion(choice,birth_date):
        if choice == 1:
            print('calculating age .....')
            time.sleep(2)
            print(f'you are {age_in_seconds(birth_date):,.0f} seconds old ')
            return True
        elif choice == 2:
            print('calculating age .....')
            time.sleep(2)
            print(f'you are {age_in_minutes(birth_date):,.0f} minutes old')
            return True
        elif choice == 3:
            print('calculating age .....')
            time.sleep(2)
            print(f'you are {age_in_hours(birth_date):,.0f} hours old')
            return True
        elif choice == 4:
            print('calculating age .....')
            time.sleep(2)
            print(f'you are {age_in_days(birth_date):,.0f} days old ')
            return True
        elif choice == 5:
            print('calculating age .....')
            time.sleep(2)
            print(f'you are {age_in_months(birth_date):,.0f} months old')
            return True
        elif choice == 6:
            print('calculating age .....')
            time.sleep(2)
            print(f'you are {age_in_years(birth_date):,.0f} years old')
            return True
        elif choice == 7:
            print('calculating age .....')
            time.sleep(2)
            table = Table(title='age in all formats')
            table.add_column('format', justify='left' , style='white')
            table.add_column('age', justify='left', style='blue')
            table.add_row('seconds', f'{age_in_seconds(birth_date):,.0f}')
            table.add_row('minutes', f'{age_in_minutes(birth_date):,.0f}')
            table.add_row('hours', f'{age_in_hours(birth_date):,.0f}')
            table.add_row('days', f'{age_in_days(birth_date):,.0f}')
            table.add_row('months', f'{age_in_months(birth_date):,.0f}')
            table.add_row('years', f'{age_in_years(birth_date):,.0f}')
            console = Console()
            console.print(table)
            return True
        elif choice == 8:
            print('calculating days .....')
            time.sleep(2)
            print(f'days to your next  birthday is [bold red underline]{days_to_birthday(birth_date)}[/bold red underline] days away')
            return True
        elif choice == 9:
            return False
        else:
            print('please enter a valid choice')
def get_date():
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
        birth_date = datetime.date(int(year), int(month), int(day))
        time.sleep(2)
        return birth_date
def get_choice():
        print_options()
        choice = int(input('enter your choice\n'))
        
        if choice > 0 and choice < 9:
                return choice
        else:
                print('please enter a valid choice')     
def age_calculator():
    while True:
        print_options()
        choice = int(input('enter your choice\n'))
        if not calculattion(choice,date):
            print('exiting app Goodbye👋👋🖐')
            break
        again = input('do you want to try other formats(yes/no) ?').strip().lower()
        if again != 'yes':
            print('exiting app Goodbye👋👋🖐')
            break   
def born_day_info(date):
    print(f'you were born on {date.day} {date.strftime("%B")}, {date.year} on a [bold red]{date.strftime("%A")}[/bold red]')
    day_facts = {
    "Monday": "People born on Monday are known for their deep empathy and nurturing spirit. They often become the emotional anchors in their communities.",
    "Tuesday": "Tuesday-born individuals are fiery and fearless. They’re natural leaders who thrive in competitive environments and love a good challenge.",
    "Wednesday": "Born communicators, Wednesday babies are witty, curious, and often brilliant at connecting ideas and people. Many great writers and thinkers share this day.",
    "Thursday": "Thursday-borns are generous visionaries. They dream big and inspire others with their optimism and wisdom—natural teachers and philosophers.",
    "Friday": "People born on Friday radiate charm and creativity. They’re lovers of beauty and harmony, often drawn to the arts and social causes.",
    "Saturday": "Saturday-born individuals are disciplined and determined. They’re the builders of legacies—quietly persistent and incredibly reliable.",
    "Sunday": "Sunday babies shine with charisma and confidence. They’re often destined for the spotlight, with a magnetic presence and a strong sense of purpose."
}
    print('[bold yellow]amazing fact about your birth day is:[/bold yellow]')
    print(f'[bold red]{day_facts[date.strftime("%A")]}[/bold red]')
print('[bold red]**********welcome to age calculator**********[/bold red]')
print('getting today\'s day .....')
time.sleep(2)
print(f'today is {datetime.date.today()} on [bold yellow]{datetime.date.today().strftime("%A")}[/bold yellow]')
date = get_date()
print(f'your date of birth is {date}')
print('loading menu .....')
time.sleep(2)
while True:
    print('select what you want')
    print('1. calculate age')
    print('2. amazing fact about your birth day\n')
    print('3. exit\n')
    option = int(input('\nenter your choice\n'))
    if option == 1:
        age_calculator()
    elif option == 2:
        print('seraching fact about your birthday')
        time.sleep(2)
        born_day_info(date)
    elif option == 3:
        print('exiting app Goodbye👋👋🖐')
        time.sleep(2)
        break
    else:
        print('please enter a valid choice')

        
