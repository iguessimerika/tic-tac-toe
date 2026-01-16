import os
import rich
from rich.prompt import Prompt

def starting_screen():
    """clears the terminal and shows the game name at the top of the terminal"""
    clear_screen()
    print(f"{"="*6} TIC TAC TOE {"="*6}\n")

    
def clear_screen():
    """clears the terminal"""
    os.system("cls" if os.name == "nt" else "clear")
    
def spacer():
    """prints a spacer for in between the board and the player entry"""
    print(f"\n\n{"="*25}\n\n")


def player_entry():
    """asks the user for 2 player names and saves them in a dictionary with their symbol and color"""
    
    player1 = input("Name Spieler 1: ")
    player2 = input("Name Spieler 2: ")
    
    player_data = {
        "player1": {
            "name": player1,
            "symbol": "X",
            "color": "blue"
        },
        "player2": {
            "name": player2,
            "symbol": "O",
            "color": "red"
        }
    }
    
    return player_data


def display_player_turn(player, color):
    """prints, which players turn it is"""
    
    rich.print(f"[{color}]{player}[/{color}], du bist dran!")


def display_board(board):
    """displays the given 2d list as the board in the terminal"""
    starting_screen()
    spacer()
    
    border = "     +---+---+---+"
    
    # top row - numbers for columns
    rich.print("[bold yellow]       1   2   3[/bold yellow]")
    print(border)
    
    curr_row = 1
    for row in board:
        rich.print(f"  {curr_row}  | {row[0]} | {row[1]} | {row[2]} |")
        print(border)
        
        curr_row += 1


def position_entry():
    """asks the player for the entry of the position"""
    while True:
        try:
            row = int(Prompt.ask("[bold cyan]Zeile[/bold cyan] angeben (1-3)"))-1
            column = int(Prompt.ask("[bold yellow]Spalte[/bold yellow] angeben (1-3)"))-1
            
            break
        except ValueError:
            print("Ungültige Zahl. Erneute Eingabe erforderlich.")
    
    return [row, column]

def position_error():
    """shows a message, if an invalid position was entered"""
    print("Inkorrekte Position, bitte erneut versuchen.")
    
def print_result(win, winner):
    """shows the winning / tie message"""
    if win:
        rich.print(f"[bold green]Glückwunsch, {winner} hat gewonnen!")
    else:
        print("Unentschieden!")

def play_again():
    """asks the user if they want to play again"""
    again = input("Erneut spielen (y/n)? ")
    
    if again != "y":
        return False
    else:
        return True