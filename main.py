import tui, game, pprint

def main():
    
    while True:
        tui.starting_screen()
    
        players = tui.player_entry()
        winner = None
        board = game.generate_board()
        
        tui.display_board(board)
        
        while True:
            for player in players:
                player_data = players.get(player)
                name = player_data.get("name")
                symbol = player_data.get("symbol")
                
                tui.spacer()
                
                tui.display_player_turn(name)
                
                while True:
                    [row, column] = tui.position_entry()
                    
                    if game.check_position(row, column, board):
                        break
                    else:
                        tui.position_error()
                        
                board = game.play_turn(board, symbol, row, column)
                
                win = game.check_win(board)
                
                print("debug")
                
                tui.display_board(board)
                
                if win:
                    winner = name
                    break
            if win:
                break
        
        tui.spacer()
                
        tui.print_winner(winner)
    
        if not tui.play_again():
            break
            
    


if __name__ == "__main__":
    main()
