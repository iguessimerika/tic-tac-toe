import tui, game, pprint

def main():
    
    while True:
        # show the game name
        tui.starting_screen()

        # get player names and data
        players = tui.player_entry()
        winner = None
        win = False
        tie = False
        # generate empty board as 2d array
        board = game.generate_board()
        
        # display board in the terminal
        tui.display_board(board)
        
        while True:
            for player in players:
                # get player data
                player_data = players.get(player)
                name = player_data.get("name")
                symbol = player_data.get("symbol")
                color = player_data.get("color")
                
                tui.spacer()
                
                # show, whose turn it is
                tui.display_player_turn(name, color)
                
                # prompt player to enter a row and column for their play
                while True:
                    [row, column] = tui.position_entry()
                    
                    # check if it was a valid position (not filled, out of bounds)
                    if game.check_position(row, column, board):
                        break
                    else:
                        tui.position_error()
                
                # update the board
                board = game.play_turn(board, symbol, row, column, color)
                
                # check if there are no more plays available
                tie = game.check_tie(board)
                
                if not tie:
                    # check for a win vertically, horizontally or diagonally
                    win = game.check_win(board)
                    
                    tui.display_board(board)
                    
                    if win:
                        winner = name
                        break
                else:
                    break
            if win or tie:
                break
        
        tui.spacer()
        
        # show the winner or a tie
        tui.print_result(win, winner)

        # ask the user to play again
        if not tui.play_again():
            break
            
    


if __name__ == "__main__":
    main()
