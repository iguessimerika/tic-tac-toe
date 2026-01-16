import re

def generate_board():
    """generates a 2d array, which is the template for an empty tic tac toe board"""
    return [[" ", " ", " "], [" ", " ", " "], [" ", " ", " "]]

def check_position(row, column, board):
    """checks if the position entered by the player is valid to play"""
    valid_position = True
    try:
        position = board[row][column]
        
        if position != " ":
            valid_position = False
    except IndexError:
        valid_position = False
        
    return valid_position

def play_turn(board, symbol, row, column, color):
    """marks the entered position with the players symbol"""
    board[row][column] = f"[{color}]{symbol}[/{color}]"
    
    return board

def check_win(board):
    """checks the board if there are three of the same symbol vertically, horizontally oder diagonally"""
    win = False
    
    # check vertically
    win = check_vertical(board)

    
    # check horizontally, if win isnt already True
    if not win:
        win = check_horizontal(board)

          
    # check diagonally, if win isnt already True
    if not win:
        win = check_diagonal(board)
            
    return win

def check_tie(board):
    """checks the board if no positions are empty and there is a tie"""
    tie = True
            
    if any(" " in row for row in board):
        tie = False
    
    return tie



def symbol(cell):
    """Returns X or O without color markers"""
    return re.sub(r"\[.*?\]", "", cell)

def is_win(cells):
    """Returns true, if there are 3 of the same symbols in a row"""
    symbols = [symbol(c) for c in cells]
    return len(set(symbols)) == 1 and symbols[0] in ("X", "O")

def highlight(cells):
    """Returns the given cells highlighted in bold green to show the win"""
    symbols = [symbol(c) for c in cells]
    return [f"[bold green]{s}[/bold green]" for s in symbols]



def check_vertical(board):
    """checks if there is a vertical win on the board"""
    win = False
    
    for r, row in enumerate(board):
        if is_win(row):
            win = True
            board[r] = highlight(row)
            break
    
    return win

def check_horizontal(board):
    """checks if there is a horizontal win on the board"""
    win = False
    
    for col in range(3):
        column = [board[r][col] for r in range(3)]
        
        if is_win(column):
            win = True
            highlighted = highlight(column)
            
            for row in range(3):
                board[row][col] = highlighted[row]
            break
    
    return win

def check_diagonal(board):
    """checks if there is a diagonal win on the board"""
    win = False
    
    # left top to right bottom (\)
    diag = [board[i][i] for i in range(3)]

    if is_win(diag):
        win = True
        h = highlight(diag)
        for i in range(3):
            board[i][i] = h[i]
    
    # right top to left bottom (/)
    if not win:
        diag = [board[row][2 - row] for row in range(3)]

        if is_win(diag):
            win = True
            h = highlight(diag)
            for row in range(3):
                board[row][2 - row] = h[row]
    
    return win