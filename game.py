import re

def generate_board():
    return [[" ", " ", " "], [" ", " ", " "], [" ", " ", " "]]

def check_position(row, column, board):
    valid_position = True
    try:
        position = board[row][column]
        
        if position != " ":
            valid_position = False
    except IndexError:
        valid_position = False
        
    return valid_position

def play_turn(board, symbol, row, column, color):
    board[row][column] = f"[{color}]{symbol}[/{color}]"
    
    return board

def check_win(board):
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
    tie = True
            
    if any(" " in row for row in board):
        tie = False
    
    return tie



def symbol(cell):
    """Returns X or O without color markers"""
    return re.sub(r"\[.*?\]", "", cell)

def is_win(cells):
    symbols = [symbol(c) for c in cells]
    return len(set(symbols)) == 1 and symbols[0] in ("X", "O")

def highlight(cells):
    symbols = [symbol(c) for c in cells]
    return [f"[bold green]{s}[/bold green]" for s in symbols]



def check_vertical(board):
    win = False
    
    for r, row in enumerate(board):
        if is_win(row):
            win = True
            board[r] = highlight(row)
            break
    
    return win

def check_horizontal(board):
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