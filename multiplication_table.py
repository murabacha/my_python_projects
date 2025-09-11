from rich.console import Console
from rich.table import Table
from rich import print
import random
import time
console = Console()
library_colors = [
    "red",
    "green",
    "blue",
    "yellow",
    "magenta",
    "cyan",
    "white",
    "bright_red",
    "bright_green",
    "bright_blue",
    "bright_yellow",
    "bright_magenta",
    "bright_cyan",
    "bright_white",
    "hot_pink",         
]
def create_table(num1, num2):
    table = Table(title="Multiplication Table")
    for i in range(1,num1 + 1):
        table.add_column(str(i) ,style=random.choice(library_colors)) 
    for i in range(1,num2 + 1):
        table.add_row(*[str(i * j) for j in range(1,num1 + 1)])
    print(f'[{random.choice(library_colors)}]creating table...[/]')
    time.sleep(5)
    console.print(table)
def create_multiplication_table(num1, num2):
    rows = []
    for i in range(1,num1 + 1):
        #for x in range(1,num1 + 1):
        rows.append([str((i * j)) for j in range(1,num1 + 1)])
    #return rows
    print(len(rows))
    for i in range(len(rows)):
        #print(rows)
        results = " - ".join(rows[i])
        print(results)
print(f"[{random.choice(library_colors)}]*******Multiplication Table Generator**************[/]\n")
print(f"[{random.choice(library_colors)}]*please note that how the table looks depends on your screen size[/]\n")
print('[bold red]for most laptops i would recomend to use the table option with a maximum of 28 columns and 36 rows[/bold red]\n')
try:
    num1 = int(input('Enter the first number:'))
except ValueError:
    print(f"[{random.choice(library_colors)}]Please enter a valid number.[/]")
    #num1 = int(input(f"[{random.choice(library_colors)}]Enter the first number: [{random.choice(library_colors)}]"))
try:
    num2 = int(input("]Enter the second number: "))
except ValueError:
    print(f"[{random.choice(library_colors)}]Please enter a valid number.[/]")
#create_table(num1, num2)
print(f"[{random.choice(library_colors)}]do you want a table or raw print[/]\n1 [{random.choice(library_colors)}]for table[/]\n2 [{random.choice(library_colors)}]for raw print[/]\n [{random.choice(library_colors)}]note that the raw print is its ugly though and hard to read[/]")
try:
    choice = int(input())
except ValueError:
    print(f"[{random.choice(library_colors)}]Please enter a valid number.[/]")
if choice == 1:
    create_table(num1, num2)
    #print("Enter the number of rows and columns:")
elif choice == 2:
    create_multiplication_table(num1, num2)