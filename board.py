# Runs the Board class
class Board:
    # Creates the 2d board that are called in battleship                                                                                                                                                                                                                                                                                                             
    # Creates board function                                                                                                                                                                                                                                                                                                                                         
    def __init__(self, size):
        # Size for how long the 2d list will be                                                                                                                                                                                                                                                                                                                      
        self.size = size
        self.game_board = []
        for i in range(size):
            row = []
            for j in range(size):
                row.append('  |')

            self.game_board.append(row)


    pass
    # Winning statement for the first player                                                                                                                                                                                                                                                                                                                         
    def first_player_winning(self, continue_till_win,player1_carrier_count, player1_battle_count, player1_crusier_count, player1_submarine_count,player1_destroyer_count):
        # Check if all the ships have been sunk or not for player 1                                                                                                                                                                                                                                                                                                  
        if player1_carrier_count == 0 and player1_battle_count == 0 and player1_crusier_count == 0 and \
                player1_submarine_count == 0 and player1_destroyer_count == 0:
            # Prints player 2 wins if all player 1 ships are zero                                                                                                                                                                                                                                                                                                    
            print('Player2 wins!')
            # Bool would be false if statement is correct                                                                                                                                                                                                                                                                                                            
            continue_till_win = False
            # Stop the game after saying who won                                                                                                                                                                                                                                                                                                                     
            return continue_till_win
        pass
        # Winning statement for the first player                                                                                                                                                                                                                                                                                                                     
    # Player 2 Winning condition                                                                                                                                                                                                                                                                                                                                     
    def second_player_winning(self, continue_till_win, player2_carrier_count, player2_battle_count,
                             player2_crusier_count, player2_submarine_count, player2_destroyer_count):
        # Check if all the ships have been sunk or not for player 1                                                                                                                                                                                                                                                                                                  
        if player2_carrier_count == 0 and player2_battle_count == 0 and player2_crusier_count == 0 and \
                player2_submarine_count == 0 and player2_destroyer_count == 0:
            # Prints player 2 wins if all player 1 ships are zero                                                                                                                                                                                                                                                                                                    
            print('Player1 wins!')
            # Bool would be false if statement is correct                                                                                                                                                                                                                                                                                                            
            continue_till_win = False
            # Stop the game after saying who won                                                                                                                                                                                                                                                                                                                     
            return continue_till_win
        pass

        pass
    # Reisters the shot when the coordinates are passed                                                                                                                                                                                                                                                                                                              
    def register_shot(self,x, y,player):
        # sees if the space is not empty                                                                                                                                                                                                                                                                                                                             
        if (self.player2.game_board[x][y]) != '  |':
            # checks if the space is not already missed                                                                                                                                                                                                                                                                                                              
            if (self.player2.game_board[x][y]) != 'MM|':
                # check if the spot has not been hit                                                                                                                                                                                                                                                                                                                 
                if (self.player2.game_board[x][y]) != 'HH|':
                    hit_name = self.ship_name_dict[self.player2.game_board[x][y]]
                    print('You landed a hit on', hit_name)
                    (self.player2.game_board[x][y]) = 'HH|'
                    (self.player2_guess_board.game_board[x][y]) = 'HH|'
                    self.battle_boards(player)

                # if already hit say that it has been hit                                                                                                                                                                                                                                                                                                            
                elif (self.player2.game_board[x][y]) == 'HH|':
                    print('you already sunk a ship there, go again')

                    return player - 1

            elif (self.player2.game_board[x][y]) == 'MM|':
                print('You already hit there and missed, go again')

                return player - 1

        elif (self.player2.game_board[x][y]) == '  |':
            print('You missed')
            (self.player2.game_board[x][y]) = 'MM|'
            (self.player2_guess_board.game_board[x][y]) = 'MM|'
        pass

