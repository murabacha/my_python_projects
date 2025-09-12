from rich.console import Console
from rich.table import Table
from rich import print
import random
console = Console()
inputs = ['[red]X[/red]', '[purple]O[/purple]']
computer_choice = random.choice(inputs)
player_choice = ''
if computer_choice == "[red]X[/red]":
    player_choice = "[purple]O[/purple]"
elif computer_choice == "[purple]O[/purple]":
    player_choice = "[red]X[/red]"
print('welcome to tic tac toe\n')
print(f'you are  {player_choice}  and the computer is  {computer_choice} \n')
position_1_1 = "1"#1
position_1_2 = "2"#2
position_1_3 = "3"#3
position_2_1 = "4"#4
position_2_2 = "5"#5
position_2_3 = "6"#6
position_3_1 = "7"#7
position_3_2 = "8"#8
position_3_3 = "9"#9
empty_positions = ["1", "2", "3", "4", "5", "6", "7", "8", "9"]
positions_empty = False
end_game = False
select_corner = True
close_game = False
def compare_positions(position_1_1, position_1_2, position_1_3, position_2_1, position_2_2, position_2_3, position_3_1, position_3_2, position_3_3):
    global end_game,empty_positions
    if position_1_1 == position_1_2 == position_1_3:
        winner = position_1_1
        end_game = True
        return winner
    elif position_2_1 == position_2_2 == position_2_3:
        winner = position_2_1
        end_game = True
        return winner
    elif position_3_1 == position_3_2 == position_3_3 :
        winner = position_3_1
        end_game = True
        return winner
    elif position_1_1 == position_2_1 == position_3_1:
        winner = position_1_1
        end_game = True
        return winner
    elif position_1_2 == position_2_2 == position_3_2:
        winner = position_1_2
        end_game = True
        return winner
    elif position_1_3 == position_2_3 == position_3_3:
        winner = position_1_3
        end_game = True
        return winner
    elif position_1_1 == position_2_2 == position_3_3:
        winner = position_1_1
        end_game = True
        return winner
    elif position_1_3 == position_2_2 == position_3_1:
        winner = position_1_3
        end_game = True
        return winner
    else:
        if not empty_positions:
            winner = 'it was a tie'
            end_game = True
            return winner
def print_table(position_1_1, position_1_2, position_1_3, position_2_1, position_2_2, position_2_3, position_3_1, position_3_2, position_3_3):
    table = Table(title="Tic Tac Toe",show_lines=True,show_header=False,show_edge=True,border_style="white")
    table.add_row(position_1_1, position_1_2, position_1_3)
    table.add_row(position_2_1, position_2_2, position_2_3)
    table.add_row(position_3_1, position_3_2, position_3_3)
    console.print(table)
def computer_position():
    global select_corner, positions_empty, computer_choice, position_1_1, position_1_2, position_1_3, position_2_1, position_2_2, position_2_3, position_3_1, position_3_2, position_3_3,empty_positions
    try:
        best_positions = ['1', '3', '7', '9']
        if '5' in empty_positions:
            choice = '5'
            empty_positions.remove(choice)
            position_2_2 = computer_choice
            return choice
        if select_corner:
            if '5' not in empty_positions and any(position in empty_positions for position in best_positions):
                best_positions_available = []
                for position in best_positions:
                    if position in empty_positions:
                        best_positions_available.append(position)
                choice = random.choice(best_positions_available)
                empty_positions.remove(choice)
                if choice == "1":
                    position_1_1 = computer_choice
                    select_corner = False
                    return choice
                elif choice == "3":
                    position_1_3 = computer_choice
                    select_corner = False
                    return choice
                elif choice == "7":
                    position_3_1 = computer_choice
                    select_corner = False
                    return choice
                elif choice == "9":
                    position_3_3 = computer_choice
                    select_corner = False
                    return choice
                return choice
            else:
                choice = random.choice(empty_positions)
                empty_positions.remove(choice)
                if choice == "2":
                    position_1_2 = computer_choice
                    select_corner = False
                    return choice
                elif choice == "4":
                    position_2_1 = computer_choice
                    select_corner = False
                    return choice
                elif choice == "6":
                    position_2_3 = computer_choice
                    select_corner = False
                    return choice
                elif choice == "8":
                    position_3_2 = computer_choice
                    select_corner = False
                    return choice
                return choice
        if not select_corner:
            choice = random.choice(empty_positions)
            empty_positions.remove(choice)
            if choice == "2":
                position_1_2 = computer_choice
                select_corner = True
                return choice
            elif choice == "4":
                position_2_1 = computer_choice
                select_corner = True
                return choice
            elif choice == "6":
                position_2_3 = computer_choice
                select_corner = True
                return choice
            elif choice == "8":
                position_3_2 = computer_choice
                select_corner = True
                return choice
    except IndexError:
        positions_empty = True
        return  
def get_player_position():
    global player_choice, positions_empty, position_1_1, position_1_2, position_1_3, position_2_1, position_2_2, position_2_3, position_3_1, position_3_2, position_3_3,empty_positions
    try:
        while True:    
            if not empty_positions:
                print("all positions are taken\n")
                positions_empty = True
                break
            choice = input(f"select a positionfrom these {empty_positions}\n") 
            if choice not in empty_positions:
                print("this position is already taken\n")
            else:
                empty_positions.remove(choice) 
                if choice == "1":
                    position_1_1 = player_choice
                    break
                elif choice == "2":
                    position_1_2 = player_choice
                    break
                elif choice == "3":
                    position_1_3 = player_choice
                    break
                elif choice == "4":
                    position_2_1 = player_choice
                    break
                elif choice == "5":
                    position_2_2 = player_choice
                    break
                elif choice == "6":
                    position_2_3 = player_choice
                    break
                elif choice == "7":
                    position_3_1 = player_choice
                    break
                elif choice == "8":
                    position_3_2 = player_choice
                    break
                elif choice == "9":
                    position_3_3 = player_choice 
                    break  
    except ValueError:
        positions_empty = True
def play_game():
    global positions_empty,player_choice,computer_choice,position_1_1, position_1_2, position_1_3, position_2_1, position_2_2, position_2_3, position_3_1, position_3_2, position_3_3,empty_positions
    #get_computer_position()
    if end_game:
        return
    print(f'computer has drawn {computer_choice} at position  {computer_position()}')
    winner = compare_positions(position_1_1, position_1_2, position_1_3, position_2_1, position_2_2, position_2_3, position_3_1, position_3_2, position_3_3)
    if winner == player_choice:
        print("\n[bold red]you won[/bold red]\n")
    elif winner == computer_choice:
        print("\n[bold red]you lost to the computer[/bold red]\n")
    else:
        if end_game:
            print("\n[bold red]its a draw[/bold red]\n")
    #print_table(position_1_1, position_1_2, position_1_3, position_2_1, position_2_2, position_2_3, position_3_1, position_3_2, position_3_3)
    if not end_game:
        print_table(position_1_1, position_1_2, position_1_3, position_2_1, position_2_2, position_2_3, position_3_1, position_3_2, position_3_3)
    if end_game:
        return
    get_player_position()
def play_misere():
    global positions_empty,player_choice,computer_choice,position_1_1, position_1_2, position_1_3, position_2_1, position_2_2, position_2_3, position_3_1, position_3_2, position_3_3,empty_positions
    print('in thin mode the first person to get 3 consecutive marks loses\n')
    if end_game:
        return
    print(f'computer has drawn  {computer_choice}  at position  {computer_position()}')
    winner = compare_positions(position_1_1, position_1_2, position_1_3, position_2_1, position_2_2, position_2_3, position_3_1, position_3_2, position_3_3)
    if winner == player_choice:
        print("\n[bold red]you lost you had the first 3 consecutive marks[/bold red]\n")
    elif winner == computer_choice:
        print("\n[bold red]you won te computer had the first 3 consecutive marks[/bold red]\n")
    else:
        if end_game:
            print("\n[bold red]its a draw[/bold red]\n")
    #print_table(position_1_1, position_1_2, position_1_3, position_2_1, position_2_2, position_2_3, position_3_1, position_3_2, position_3_3)
    if not end_game:
        print_table(position_1_1, position_1_2, position_1_3, position_2_1, position_2_2, position_2_3, position_3_1, position_3_2, position_3_3)
    if end_game:
        return
    get_player_position()
while True:
    if close_game:
        break
    while True:
        print('enter the mode you want to play\n1: for normal tic-tac-toe\n2: for misere tic-tac-toe\n3: to exit')
        try:
            mode = int(input())
        except ValueError:
            print('\n[bold red]i can see you entering letters[/bold red]\n')
            print('\n[bold red]please enter a valid number[/bold red]\n')
        if mode == 1:
            while True:
                if positions_empty :
                    break
                if end_game:
                    print_table(position_1_1, position_1_2, position_1_3, position_2_1, position_2_2, position_2_3, position_3_1, position_3_2, position_3_3)
                    break
                play_game()
                continue
        elif mode == 2:
            while True:
                if positions_empty :
                    break
                if end_game:
                    print_table(position_1_1, position_1_2, position_1_3, position_2_1, position_2_2, position_2_3, position_3_1, position_3_2, position_3_3)
                    break
                play_misere()
                continue
        elif mode == 3:
            print('\n[bold red]goodbye[/bold red]\n')
            close_game = True
            break
        else:
            print('\n[bold red]please enter a valid number[/bold red]\n')
            continue
        print('do you want to play again? enter (no ) to exit')
        again = input().strip().lower()
        if again == 'no':
            break
        else:
            position_1_1 = "1"#1
            position_1_2 = "2"#2
            position_1_3 = "3"#3
            position_2_1 = "4"#4
            position_2_2 = "5"#5
            position_2_3 = "6"#6
            position_3_1 = "7"#7
            position_3_2 = "8"#8
            position_3_3 = "9"#9
            empty_positions = ["1", "2", "3", "4", "5", "6", "7", "8", "9"]
            positions_empty = False
            end_game = False
            select_corner = True
            computer_choice = random.choice(inputs)
            if computer_choice == "[red]X[/red]":
                player_choice = "[purple]O[/purple]"
            elif computer_choice == "[purple]O[/purple]":
                player_choice = "[red]X[/red]"
            print(f'you are {player_choice} and the computer is {computer_choice}')