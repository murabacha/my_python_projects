import time
from rich import print

def celcius_to_fahrenheit(celcius):
    fahrenheit = (celcius * 9/5) + 32
    return fahrenheit
def fahrenheit_to_celcius(fahrenheit):
    celcius = (fahrenheit - 32) * 5/9
    return celcius
def celcius_to_kelvin(celcius):
    kelvin = celcius + 273.15
    return kelvin
def kelvin_to_celcius(kelvin):
    celcius = kelvin - 273.15
    return celcius
def fahrenheit_to_kelvin(fahrenheit):
    kelvin = (fahrenheit - 32) * 5/9 + 273.15
    return kelvin
def kelvin_to_fahrenheit(kelvin):
    fahrenheit = (kelvin - 273.15) * 9/5 + 32
    return fahrenheit
def print_function():
    print("1: celcius_to_fahrenheit")
    print('2: fahrenheit_to_celcius')
    print('3: celcius_to_kelvin')
    print('4: kelvin_to_celcies')
    print('5: fahrenheit to kelvin ')
    print('6: kelvin to fahreinheit')
def calculate(choice):
    if choice == 1:
        celcius = float(input('enter celcius value (°C) (please enter number only)\n'))
        print('calculating...')
        time.sleep(2)
        print(f'{celcius} [bold yellow]celcius[/bold yellow] is {celcius_to_fahrenheit(celcius):,.2f} [bold red]fahrenheit[bold red]') #celcius_to_fahrenheit(celcius)
        return True
    elif choice == 2:
        fahrenheit = float(input('enter fahrenheit value (°C) (please enter number only)\n'))
        print('calculating...')
        time.sleep(2)
        print(f'{fahrenheit} [bold yellow]fahrenheit[/bold yellow] is {fahrenheit_to_celcius(fahrenheit):,.2f} [bold red]celcius[bold red]') #fahrenheit_to_celcius(fahrenheit)
        return True
    elif choice == 3:
        celcieus = float(input('enter celcius value (°C) (please enter number only)\n'))
        print('calculating...')
        time.sleep(2)
        print(f'{celcieus}[bold yellow] celcius[/bold yellow] is {celcius_to_kelvin(celcieus):,.2f} [bold red]kelvin[bold red]') #celcius_to_kelvin(celcieus)
        return True
    elif choice == 4:
        kelvin = float(input('enter kelvin value (°C) (please enter number only)\n'))
        print('calculating....')
        time.sleep(2)
        print(f'{kelvin} [bold yellow]kelvin[/bold yellow] is {kelvin_to_celcius(kelvin):,.2f} [bold red]celcius[bold red]') #kelvin_to_celcius(kelvin)
        return True
    elif choice == 5:
        fahrenheit = float(input('enter fahrenheit value (°C) (please enter number only)\n'))
        print('calculating...')
        time.sleep(2)
        print(f'{fahrenheit} [bold yellow]fahrenheit[/bold yellow] is {fahrenheit_to_kelvin(fahrenheit):,.2f} [bold red]kelvin[bold red]') #fahrenheit_to_kelvin(fahrenheit)
        return True
    elif choice == 6:
        kelvin = float(input('enter kelvin value (°C) (please enter number only)\n'))
        print('calculating...')
        time.sleep(2)
        print(f'{kelvin} [bold yellow]kelvin[/bold yellow] is {kelvin_to_fahrenheit(kelvin):,.2f} [bold red]fahrenheit[bold red]') #kelvin_to_fahrenheit(kelvin)
        return True
    elif choice == 7:
        print('exiting app Goodbye👋👋🖐')
        time.sleep(2)
        return False
        
    else:
        print('please enter a valid choice')
print('loading program......')
time.sleep(2)
print('\n')
print('[bold red]**********Welcome to the temparature converter**********[/bold red]')
print('\n')
while True:
    
    print('select what you want to convert')
    print_function()
    choice = int(input('enter your choice\n '))
    if not calculate(choice):
        print('exiting program Goodbye👋👋🖐')
        time.sleep(2)
        break

    again = input('do you want to try other formats(yes/no) ?').strip().lower()
    if again != 'yes':
        print('exiting program Goodbye👋👋🖐')
        time.sleep(2)
        break
   
