
import board

# RUNS THE BATTLESHIP GAME                                                                                                                                                                                                                    
class BattleshipGame:
    # CREATES THE BOARD OBJECT AND OTHER Self OBJECTS                                                                                                                                                                                         
  def __init__(self, size=10):
    # Creates all the objects needed for the projects                                                                                                                                                                                     
    self.size = size
    # Player 1 boards being created in the boards file                                                                                                                                                                                    
    self.player1 = board.Board(size)
    # player 2 board being created in the board file                                                                                                                                                                                      
    self.player2 = board.Board(size)
    # use for the turn counter                                                                                                                                                                                                            
    self.turn_count = 2
    # dict holding the ship positions                                                                                                                                                                                                     
    self.player1_ships = {}
    self.player2_ships = {}
    self.open_space = '  |'
    # deciding active boards empty boards                                                                                                                                                                                                 
    self.player1_guess_board = board.Board(size)
    self.player2_guess_board = board.Board(size)
    # dict with the names of ship both the short term and the full name                                                                                                                                                                   
    self.ship_name_dict = {'Ca|': 'Carrier', 'Bt|': 'Battleship', 'Cr|': 'Cruiser', 'Sb|': 'Submarine',
                            'Ds|': 'Destroyer'}

    pass

  def place_ships(self, player_board, ship, player):
    # bool value for the while loop                                                                                                                                                                                                                                                                                                                                                                                                                                                     
    is_valid_position = False
    # List holding information on the ship location that would be sent to the self.player dict                                                                                                                                                                                                                                                                                                                                                                                          
    place1_ship = []
    place2_ship = []

    while not is_valid_position:
        # display board after printing the ship on it                                                                                                                                                                                                                                                                                                                                                                                                                                   
        self.display_boards(player)
        # get user input and split it to get the coordinates                                                                                                                                                                                                                                                                                                                                                                                                                            
        print('Enter x y coordinates to place the ', end='')
        print(ship['name'], end='')
        cord = input(' : ')
        cord = cord.split(' ')
        length = int(cord[0])
        width = int(cord[1])
        # check if left or right                                                                                                                                                                                                                                                                                                                                                                                                                                                        
        left_right = input('Enter Right or Down (r or d) ')
        # check to see if the coordinates are inside the range and if they are anything other then r or l                                                                                                                                                                                                                                                                                                                                                                               
        if length > 10 or length < 0 and width > 10 or width < 0 and left_right != 'r' and left_right != 'd':
            # if true go back to the loop                                                                                                                                                                                                                                                                                                                                                                                                                                               
            is_valid_position = False
        else:
            is_valid_position = True
        # if right                                                                                                                                                                                                                                                                                                                                                                                                                                                                      
        if is_valid_position and left_right == 'r':
            for x in range(length, length + ship['size']):
                # for loop with the range of the ship size                                                                                                                                                                                                                                                                                                                                                                                                                              
                # check all coordinates to the right of the starting coordinates to see if they are open                                                                                                                                                                                                                                                                                                                                                                                
                if player_board.game_board[width][x] != self.open_space:
                    # if not restart loop                                                                                                                                                                                                                                                                                                                                                                                                                                               
                    is_valid_position = False
        # if down
        if is_valid_position and left_right == 'd':
          
            # Checks to see if they spots are open=
            for x in range(width, width + ship['size']):
                if player_board.game_board[x][length] != self.open_space:
                  
                    # if not open restart loop
                    is_valid_position = False
                  
        # if its false print invalid positions
        if not is_valid_position:
            print('Invalid position or overlapping ships, try again.')
          
        # changes the actual grid after confirming coordinates are accurate
        else:
          
            # if right
            if left_right == 'r':
                for x in range(length, length + ship['size']):
                  
                    # for the range of the ship size all coordinates equal ship symbol
                    player_board.game_board[width][x] = ship['symbol']
                    if player == 0:
                      
                        # add coordinates to the list
                        place1_ship.append([x, width])

                    else:
                      
                        # player 2
                        place2_ship.append([x, width])
                if player == 0:
                  
                    # self player equals the list makes it into a 2d list
                    self.player1_ships[ship['name']] = place1_ship
                else:
                  
                    # player_2 2d list
                    self.player2_ships[ship['name']] = place2_ship
                  
            # same thing for down
            if left_right == 'd':
                for x in range(width, width + ship['size']):
                    player_board.game_board[x][length] = ship['symbol']
                    if player == 0:
                        place1_ship.append([length, x])

                    else:
                        place2_ship.append([length, x])
                if player == 0:
                  
                    # add coordinates to the self player dict
                    self.player1_ships[ship['name']] = place1_ship
                else:
                    self.player2_ships[ship['name']] = place2_ship

    # RUNS THE WHOLE GAME(Main code)                                                                                                                                                                                                                                                                                                                                                                                                                                                        
  def run_game(self):
    # board.Board(10)
  
    # All info on the ships for the place ship function in Dict format
    carrier = {'name': 'Carrier', 'symbol': 'Ca|', 'size': 5}
    battleship = {'name': 'Battleship', 'symbol': 'Bt|', 'size': 4}
    cruiser = {'name': 'Cruiser', 'symbol': 'Cr|', 'size': 3}
    submarine = {'name': 'Submarine', 'symbol': 'Sb|', 'size': 3}
    destroyer = {'name': 'Destroyer', 'symbol': 'Ds|', 'size': 2}
    print('Player 1, prepare to place your fleet.')
    # Int value to register player 1's values first                                                                                                                                                                                                                                                                                                                                                                                                                                     
    player = 0
    # Send in each ships info and player, as well as the counter
    # places carrier for player 1
  
    self.place_ships(self.player1, carrier, player)
    # places battleship for player 1 and onwards...                                                                                                                                                                                                                                                                                                                                                                                                                                     
    self.place_ships(self.player1, battleship, player)
    self.place_ships(self.player1, cruiser, player)
    self.place_ships(self.player1, submarine, player)
    self.place_ships(self.player1, destroyer, player)
    self.turn_count += 1
    # displays the players board                                                                                                                                                                                                                                                                                                                                                                                                                                                        
    self.display_boards(player)
    # places player 2's ships now                                                                                                                                                                                                                                                                                                                                                                                                                                                       
    print('Player 2, prepare to place your fleet.')
    # counter equals 1 letting player2 ships register                                                                                                                                                                                                                                                                                                                                                                                                                                   
    player = 1
    # places player 2's carrier                                                                                                                                                                                                                                                                                                                                                                                                                                                         
    self.place_ships(self.player2, carrier, player)
    # places player 2's battleships and onwards..                                                                                                                                                                                                                                                                                                                                                                                                                                       
    self.place_ships(self.player2, battleship, player)
    self.place_ships(self.player2, cruiser, player)
    self.place_ships(self.player2, submarine, player)
    self.place_ships(self.player2, destroyer, player)
    # Displays the last ship put on the 2d players grid                                                                                                                                                                                                                                                                                                                                                                                                                                 
    self.display_boards(player)
    # print the first player's grid with ships and the second players map empty to let the player 1 choose a spot to hit                                                                                                                                                                                                                                                                                                                                                                
    self.active_board(0)
    self.turn_count += 1
    # bool function for the win statement while loop                                                                                                                                                                                                                                                                                                                                                                                                                                    
    continue_till_win = True
    # int value for taking turns if % 2 ==0 player 1 so player = 2                                                                                                                                                                                                                                                                                                                                                                                                                      
    player = 2
    # runs till all the ships on one of the boards is sunken                                                                                                                                                                                                                                                                                                                                                                                                                            
    while continue_till_win:
        # Player 1s turn                                                                                                                                                                                                                                                                                                                                                                                                                                                                
        if player % 2 == 0:
            print('Player 1s turn')
            # Takes user input to pick the coordinate to fire                                                                                                                                                                                                                                                                                                                                                                                                                           
            take_shot = input('Enter x y coordinates to fire: ')
            # splits to put them in a seperate list                                                                                                                                                                                                                                                                                                                                                                                                                                     
            take_shot = take_shot.split(' ')
            # make them equal to an int and pass it on to register hit function                                                                                                                                                                                                                                                                                                                                                                                                         
            y = int(take_shot[0])
            x = int(take_shot[1])
            # print the board and also returns the count variable responsible for invalid turns                                                                                                                                                                                                                                                                                                                                                                                         
            player = self.register_shot(x, y, player)
            # Add one to count after tuen                                                                                                                                                                                                                                                                                                                                                                                                                                               
            player += 1
        # display battle boards which show the players board with ships and the empty enemy board after turn                                                                                                                                                                                                                                                                                                                                                                            
        self.active_board(player)
        # player 2s turn                                                                                                                                                                                                                                                                                                                                                                                                                                                                
        # same functionality as player 1's                                                                                                                                                                                                                                                                                                                                                                                                                                              
        if player % 2 != 0:
            print('Player 2s turn')
            take_shot = input('Enter x y coordinates to fire: ')
            take_shot = take_shot.split(' ')
            y = int(take_shot[0])
            x = int(take_shot[1])
            player = self.register_shot(x, y, player)
            player += 1
        self.active_board(player)
        # Main WIN Condition                                                                                                                                                                                                                                                                                                                                                                                                                                                            
        # All these Count Variables track how many parts of a ship are left if all the ship part for a player is zero the,                                                                                                                                                                                                                                                                                                                                                              
        # other player wins                                                                                                                                                                                                                                                                                                                                                                                                                                                             
        player1_carrier_count = 0
        player1_battle_count = 0
        player1_crusier_count = 0
        player1_submarine_count = 0
        player1_destroyer_count = 0
        player2_carrier_count = 0
        player2_battle_count = 0
        player2_crusier_count = 0
        player2_submarine_count = 0
        player2_destroyer_count = 0
        # keeps in track the number of ships on each board after they have been reset so they can be checked                                                                                                                                                                                                                                                                                                                                                                            
        # iterates through the whole grid for player 1 to check how many ships have been sunk                                                                                                                                                                                                                                                                                                                                                                                           
        for each in range(len(self.player1.game_board)):
            for each_element in range(len(self.player1.game_board[each])):
                if self.player1.game_board[each][each_element] == 'Ca|':
                    # add 1 to the counter that tracks it if the ship symbol is on the board                                                                                                                                                                                                                                                                                                                                                                                            
                    # same for the rest of the ships for player 1                                                                                                                                                                                                                                                                                                                                                                                                                       
                    player1_carrier_count += 1
                if self.player1.game_board[each][each_element] == 'Bt|':
                    player1_battle_count += 1
                if self.player1.game_board[each][each_element] == 'Cr|':
                    player1_crusier_count += 1
                if self.player1.game_board[each][each_element] == 'Sb|':
                    player1_submarine_count += 1
                if self.player1.game_board[each][each_element] == 'Ds|':
                    player1_destroyer_count += 1
        # if all the count variables equal zero that means all the ships have been sunk for the given board and the other board wins                                                                                                                                                                                                                                                                                                                                                    
        # checks if all the ships for player1 have been sunk                                                                                                                                                                                                                                                                                                                                                                                                                            
        if player1_carrier_count == 0 and player1_battle_count == 0 and player1_crusier_count == 0 and \
                player1_submarine_count == 0 and player1_destroyer_count == 0:
                print('Player2 wins!')
                # Stop the game after saying who won                                                                                                                                                                                                                                                                                                                                                                                                                                    
                continue_till_win = False
        # iterates through the grid of player 2 to check how many ships have been sunk                                                                                                                                                                                                                                                                                                                                                                                                  
        for each in range(len(self.player2.game_board)):
            for each_element in range(len(self.player2.game_board[each])):
                if self.player2.game_board[each][each_element] == 'Ca|':
                    player2_carrier_count += 1
                if self.player2.game_board[each][each_element] == 'Bt|':
                    player2_battle_count += 1
                if self.player2.game_board[each][each_element] == 'Cr|':
                    player2_crusier_count += 1
                if self.player2.game_board[each][each_element] == 'Sb|':
                    player2_submarine_count += 1
                if self.player2.game_board[each][each_element] == 'Ds|':
                    player2_destroyer_count +=1
        # checks if all the ships for player2 have been sunk                                                                                                                                                                                                                                                                                                                                                                                                                            
        if player2_carrier_count == 0 and player2_battle_count == 0 and player2_crusier_count == 0 and \
                player2_submarine_count == 0 and player2_destroyer_count == 0:
                print('Player1 wins!')
                # stop game after saying who won                                                                                                                                                                                                                                                                                                                                                                                                                                        
                continue_till_win = False


  # REGISTERS THE SHOT ON THE BOARD FOR THE PLAYER                                                                                                                                                                                                                                                                                                                                                                                                                                        
  def register_shot(self, x, y, player):
    # Player 1s turn if player % 2==0                                                                                                                                                                                                                                                                                                                                                                                                                                                   
    if player % 2 == 0:
        # First checks to see if the coordinates given are not open space                                                                                                                                                                                                                                                                                                                                                                                                               
        if (self.player2.game_board[x][y]) != '  |':
            # Second checks to see if the coordinates is not a previous miss                                                                                                                                                                                                                                                                                                                                                                                                            
            if (self.player2.game_board[x][y]) != 'MM|':
                # Third check to see of it has not already been hit                                                                                                                                                                                                                                                                                                                                                                                                                     
                if (self.player2.game_board[x][y]) != 'HH|':
                    # if true then [x][y] is = Hit                                                                                                                                                                                                                                                                                                                                                                                                                                      
                    # used to find the key in the player dict where the coordinates are located                                                                                                                                                                                                                                                                                                                                                                                         
                    hit_name = self.ship_name_dict[self.player2.game_board[x][y]]
                    print('You landed a hit on', hit_name)
                    (self.player2.game_board[x][y]) = 'HH|'
                    (self.player2_guess_board.game_board[x][y]) = 'HH|'
                    # Print the board after saying it has been hit                                                                                                                                                                                                                                                                                                                                                                                                                      
                    self.active_board(player)

                # if it has already been hit then ask the person to go again                                                                                                                                                                                                                                                                                                                                                                                                            
                elif (self.player2.game_board[x][y]) == 'HH|':
                    print('you already sunk a ship there, go again')
                    # return player value after subtracting one so they can go again                                                                                                                                                                                                                                                                                                                                                                                                    
                    return player-1
            # if it has already been guessed before then ask to go again                                                                                                                                                                                                                                                                                                                                                                                                                
            elif (self.player2.game_board[x][y]) == 'MM|':
                print('You already hit there and missed, go again')
                # subtract one to go again                                                                                                                                                                                                                                                                                                                                                                                                                                              
                return player-1
        # if it is an open space that means the person missed                                                                                                                                                                                                                                                                                                                                                                                                                           
        elif (self.player2.game_board[x][y]) == '  |':
            # say the person missed                                                                                                                                                                                                                                                                                                                                                                                                                                                     
            print('You missed')
            # Mark MM on the board for miss                                                                                                                                                                                                                                                                                                                                                                                                                                             
            (self.player2.game_board[x][y]) = 'MM|'
            (self.player2_guess_board.game_board[x][y]) = 'MM|'

            # self.active_board(player)                                                                                                                                                                                                                                                                                                                                                                                                                                                 
    # Same format and function as the one user above for player 1                                                                   
    if player % 2 != 0:
        if (self.player1.game_board[x][y]) != '  |':
            if (self.player1.game_board[x][y]) != 'MM|':
                if (self.player1.game_board[x][y]) != 'HH|':
                    hit_name = self.ship_name_dict[self.player1.game_board[x][y]]
                    print('You landed a hit on', hit_name)
                    (self.player1.game_board[x][y]) = 'HH|'
                    (self.player1_guess_board.game_board[x][y]) = 'HH|'
                    self.active_board(player)
                elif (self.player1.game_board[x][y]) == 'HH|':
                    print('you already sunk a ship there, go again')
                    return player-1
            elif (self.player1.game_board[x][y]) == 'MM|':
                print('You already hit there and missed, go again')
                return player-1
        elif (self.player1.game_board[x][y]) == '  |':
            print('You missed')
            (self.player1.game_board[x][y]) = 'MM|'
            (self.player1_guess_board.game_board[x][y]) = 'MM|'
    return player
# FUNCTION RESPONSIBLE FOR PRINTING OUT THE PLAYER 1 AND PLAYER 2 BOARD                                                                                                                                                                                                                                                                                                                                                                                                                 
  def display_boards(self, player):
    # Player 1's turn if player % 2==0                                                                                                                                                                                                                                                                                                                                                                                                                                                  
    if player % 2 == 0:
        # prints out the number grid first                                                                                                                                                                                                                                                                                                                                                                                                                                              
        print('  0', '  1', '  2', '  3', '  4', '  5', '  6', '  7', '  8', '  9')
        # Nested for loop going through and printing each row of the 2d list for player 1                                                                                                                                                                                                                                                                                                                                                                                               
        for x in range(10):
            print(x, end=' ')
            for y in range(10):
                print(self.player1.game_board[x][y], end=' ')
            print()
    # if player %2 !=0                                                                                                                                                                                                                                                                                                                                                                                                                                                                  
    else:
        # prints out the number grid                                                                                                                                                                                                                                                                                                                                                                                                                                                    
        print('  0', '  1', '  2', '  3', '  4', '  5', '  6', '  7', '  8', '  9')
        for x in range(10):
            print(x, end=' ')
            for y in range(10):
                print(self.player2.game_board[x][y], end=' ')
            print()
# RESPONSIBLE FOR FIGURING OUT THE ACTIVE BOARD AND UNACTIVE BOARD      
  def active_board(self, player):
    # Player1's tuen                                                                                                                                                                                                                                                                               
    if player % 2 == 0:
        # Kinda prints the Board next to each other                                                                                                                                                                                                                                                                                                                                                                                                                                     
        # string1 = []                                                                                                                                                                                                                                                                                                                                                                                                                                                                  
        # string1.append(['  0', '  1', '  2', '  3', '  4', '  5', '  6', '  7', '  8', '  9'])                                                                                                                                                                                                                                                                                                                                                                                        
        # string1.append(['  0', '  1', '  2', '  3', '  4', '  5', '  6', '  7', '  8', '  9'])                                                                                                                                                                                                                                                                                                                                                                                        
        #                                                                                                                                                                                                                                                                                                                                                                                                                                                                               
        # for x in range(10):                                                                                                                                                                                                                                                                                                                                                                                                                                                           
        #     string_1 = []                                                                                                                                                                                                                                                                                                                                                                                                                                                             
        #     string_2 = []                                                                                                                                                                                                                                                                                                                                                                                                                                                             
        #     string_1.append(str(x))                                                                                                                                                                                                                                                                                                                                                                                                                                                   
        #     string_2.append(str(x))                                                                                                                                                                                                                                                                                                                                                                                                                                                   
        #     for y in range(10):                                                                                                                                                                                                                                                                                                                                                                                                                                                       
        #         string_1.append(self.player1.game_board[x][y])                                                                                                                                                                                                                                                                                                                                                                                                                        
        #         string_2.append(self.player2_guess_board.game_board[x][y])                                                                                                                                                                                                                                                                                                                                                                                                            
        #     string1.append(string_1)                                                                                                                                                                                                                                                                                                                                                                                                                                                  
        #     string1.append(string_2)                                                                                                                                                                                                                                                                                                                                                                                                                                                  
        # counter = 0                                                                                                                                                                                                                                                                                                                                                                                                                                                                   
        # while counter <= len(string1):                                                                                                                                                                                                                                                                                                                                                                                                                                                
        #     if counter + 1 < len(string1):                                                                                                                                                                                                                                                                                                                                                                                                                                            
        #         print(string1[counter], end='\t\t')                                                                                                                                                                                                                                                                                                                                                                                                                                   
        #         print(string1[counter + 1])                                                                                                                                                                                                                                                                                                                                                                                                                                           
        #         counter += 2                                                                                                                                                                                                                                                                                                                                                                                                                                                          
        # Prints the active board                                                                                                                                                                                                                                                                                                                                                                                                                                                       
        print('  0', '  1', '  2', '  3', '  4', '  5', '  6', '  7', '  8', '  9')
        for x in range(10):
            print(x, end=' ')
            for y in range(10):
                print(self.player1.game_board[x][y], end=' ')
            print()
        # prints the unactive board                                                                                                                                                                                                                                                                                                                                                                                                                                                     
        print('  0', '  1', '  2', '  3', '  4', '  5', '  6', '  7', '  8', '  9')
        for x in range(10):
            print(x, end=' ')
            for y in range(10):
                print(self.player2_guess_board.game_board[x][y], end=' ')
            print()
    # Player 2s tuen                                                                                                                                                                                                                                                                                                                                                                                                                                                                    
    if player % 2 != 0:
        # Prints the active board                                                                                                                                                                                                                                                                                                                                                                                                                                                       
        print('  0', '  1', '  2', '  3', '  4', '  5', '  6', '  7', '  8', '  9')
        for x in range(10):
            print(x, end=' ')
            for y in range(10):
                print(self.player2.game_board[x][y], end=' ')
            print()
        # prints the unactive board                                                                                                                                                                                                                                                                                                                                                                                                                                                     
        print('  0', '  1', '  2', '  3', '  4', '  5', '  6', '  7', '  8', '  9')
        for x in range(10):
            print(x, end=' ')
            for y in range(10):
                print(self.player1_guess_board.game_board[x][y], end=' ')
            print()

# If main statement                                                                                                                                                                                                                                                                                                                                                                                                                                                                         
if __name__ == '__main__':
    BattleshipGame().run_game()


