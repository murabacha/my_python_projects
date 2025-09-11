from rich.console import Console
from rich.table import Table
from rich import print
import random
console = Console()
inputs = ['X', '[purple]O[/purple]']
computer_choice = random.choice(inputs)
if computer_choice == "X":
    player_choice = "O"
else:
    player_choice = "[red]X[/red]"
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
def get_computer_position():
    global positions_empty, computer_choice, position_1_1, position_1_2, position_1_3, position_2_1, position_2_2, position_2_3, position_3_1, position_3_2, position_3_3,empty_positions
    try:
        choice = random.choice(empty_positions)
        empty_positions.remove(choice)
        if choice == "1":
            position_1_1 = computer_choice
            return choice
        elif choice == "2":
            position_1_2 = computer_choice
            return choice
        elif choice == "3":
            position_1_3 = computer_choice
            return choice
        elif choice == "4":
            position_2_1 = computer_choice
            return choice
        elif choice == "5":
            position_2_2 = computer_choice
            return choice
        elif choice == "6":
            position_2_3 = computer_choice
            return choice
        elif choice == "7":
            position_3_1 = computer_choice
            return choice
        elif choice == "8":
            position_3_2 = computer_choice
            return choice
        elif choice == "9":
            position_3_3 = computer_choice
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
    print_table(position_1_1, position_1_2, position_1_3, position_2_1, position_2_2, position_2_3, position_3_1, position_3_2, position_3_3)
    print(f'computer has drawn {computer_choice}\n at position{get_computer_position()}')
    print_table(position_1_1, position_1_2, position_1_3, position_2_1, position_2_2, position_2_3, position_3_1, position_3_2, position_3_3)
    if end_game:
        return
    get_player_position()
    winner = compare_positions(position_1_1, position_1_2, position_1_3, position_2_1, position_2_2, position_2_3, position_3_1, position_3_2, position_3_3)
    if winner == player_choice:
        print("you won")
    elif winner == computer_choice:
        print("you lost to the computer")
    else:
        if end_game:
            print("its a draw")
while True:
    while True:
        if positions_empty :
            break
        if end_game:
            break
        play_game()
    print('do you want to play again?')
    again = input().strip().lower()
    if again != 'yes':
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
        computer_choice = random.choice(inputs)
        if computer_choice == "X":
            player_choice = "O"
        else:
            player_choice = "X"