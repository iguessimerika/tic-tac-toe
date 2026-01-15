import os

def starting_screen():
    print(f"{"="*6} TIC TAC TOE {"="*6}")

    
def clear_screen():
    os.system("cls" if os.name == "nt" else "clear")
    
def spacer():
    print(f"\n\n{"="*25}\n\n")


def player_entry():
    
    player1 = input("Name Spieler 1: ")
    player2 = input("Name Spieler 2: ")
    
    player_data = {
        "player1": {
            "name": player1,
            "symbol": "X"
        },
        "player2": {
            "name": player2,
            "symbol": "O"
        }
    }
    
    return player_data


def display_player_turn(player):
    print(f"{player}, du bist dran!")


def display_board(board):
    clear_screen()
    
    border = "     +---+---+---+"
    
    # top row - numbers for columns
    print("       1   2   3")
    print(border)
    
    curr_row = 1
    for row in board:
        print(f"  {curr_row}  | {row[0]} | {row[1]} | {row[2]} |")
        print(border)
        
        curr_row += 1


def position_entry():
    while True:
        try:
            row = int(input("Zeile angeben (1-3): "))-1
            column = int(input("Spalte angeben (1-3): "))-1
            
            break
        except ValueError:
            print("Bitte eine gültige Zahl eingeben.")
    
    return [row, column]

def position_error():
    print("Inkorrekte Position, bitte erneut versuchen.")
    
def print_winner(name):
    print(f"Glückwunsch, {name} hat gewonnen!")

def play_again():
    again = input("Erneut spielen (y/n)? ")
    
    if again != "y":
        return False
    else:
        return True