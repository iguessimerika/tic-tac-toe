
def generate_board():
    return [["X", " ", " "], [" ", "X", " "], [" ", " ", " "]]

def check_position(row, column, board):
    valid_position = True
    try:
        position = board[row][column]
        
        if position != " ":
            valid_position = False
    except IndexError:
        valid_position = False
        
    return valid_position

def play_turn(board, symbol, row, column):
    board[row][column] = symbol
    
    return board

def check_win(board):
    win = False
    
    # check vertically
    for row in board:
        comp_row = "".join(row)
        
        if comp_row == "XXX" or comp_row == "OOO":
            win = True
            break
    print("debug0")  
    # check horizontally, if win isnt already True
    if not win:
        column = 0
        while column < 3:
            comp_col = board[0][column] + board[1][column] + board[2][column]
            if comp_col == "XXX" or comp_col == "OOO":
                win = True
                break
            column += 1
          
    print("debug1")  
    # check diagonally, if win isnt already True
    if not win: 
        diag1 = board[0][0] + board[1][1] + board[2][2]
        diag2 = board[0][2] + board[1][1] + board[2][0]
        
        if diag1 == "XXX" or diag1 == "OOO" or diag2 == "XXX" or diag2 == "OOO":
            win = True
            
        
    print("debug2")  
            
    return win