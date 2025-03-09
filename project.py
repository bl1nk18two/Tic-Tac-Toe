""" 
TIC TAC TOE
"""

from time import sleep
import random


class Players:
    def __init__(self):
        self.player1_name = 'Player'
        self.player1_symbol = 'X'
        self.player2_name = 'Machine'
        self.player2_symbol = 'O'

        self.players = {
            self.player1_name: self.player1_symbol,
            self.player2_name: self.player2_symbol,
        }

        if random.choice([True, False]):
            self.players = dict(sorted(self.players.items()))        


class Display(Players):
    def __init__(self):
        super().__init__()

        self.index_pattern = {
                1: [1, ''],
                2: [5, ''],
                3: [9, ''],
                4: [23, ''],
                5: [27, ''],
                6: [31, ''],
                7: [45, ''],
                8: [49, ''],
                9: [53, ''],
            }
        self.winner = None

        self.board = generate_board()

    def moves(self, move_index, player_symbol):
        if 0 < int(move_index) <= 9:


            move = self.index_pattern[move_index][0]

            if self.index_pattern[move_index][1] == '':
                self.board[move] = player_symbol
                self.index_pattern[move_index][1] = player_symbol
                return True
            else:
                return 'Invalid Move. Try Again'
        else:
            return 'Invalid Move. Try Again.'
        
    def turn(self):

        for player, symbol in self.players.items():
            if player == self.player1_name:

                turn_message = None
                while not turn_message is True:
                    try:
                        move = int(str(input("It's your turn: ").strip()))
                    except ValueError:
                        print('Must Enter Digits Between 1 and 9\n')
                    else:
                        turn_message = self.moves(move, symbol)
                        if isinstance(turn_message, str):
                            print(turn_message)
                        else:
                            if winner := check_winner(self.index_pattern, self.player1_symbol, self.player2_symbol):
                                self.winner = winner
                                show_board(self.board)   
                                return 
                            show_board(self.board)
            
            else:
                sleep(0.4)
                invalid_number = True
                while invalid_number:
                    move = random.randint(1, 9)
                    if self.index_pattern[move][1] == '':
                        invalid_number = False

                _ = self.moves(move, symbol)    
                if winner := check_winner(self.index_pattern, self.player1_symbol, self.player2_symbol):
                    self.winner = winner
                    show_board(self.board)   
                    return                     
                show_board(self.board)    


def main():
    table = Display()

    show_board(table.board)

    while table.winner is None:
        table.turn()


    if table.winner == 'draw':
        print("Cat's Game")
    else:
        print(f'{table.winner} Wins!!')


def check_winner(index_pattern, player1_symbol, player2_symbol):
    
    patterns = [
        [1, 2, 3], [4, 5, 6], [7, 8, 9],  
        [1, 4, 7], [2, 5, 8], [3, 6, 9],  
        [1, 5, 9], [3, 5, 7]             
    ]

    for pattern in patterns:
        values = [index_pattern[i][1] for i in pattern]
        if values == [player1_symbol] * 3:
            return 'Player'
        elif values == [player2_symbol] * 3:
            return 'Machine'

    if all(index_pattern[i][1] != '' for i in index_pattern):
        return 'draw'
    
    return None


def show_board(board):
    table = ''
    counter = 0

    for i in board:
        table += i  
        counter += 1
        
        if counter == 11:
            table += '\n'
            counter = 0 

    print(table)


def generate_board():
    first_pattern = ['|' if i in (3, 7) else ' ' for i in range(11)]
    second_pattern = ['|' if i in (3, 7) else '-' for i in range(11)]        

    table = [
        ''.join(first_pattern), 
        ''.join(second_pattern), 
        ''.join(first_pattern),  
        ''.join(second_pattern), 
        ''.join(first_pattern)   
    ]

    return [i for x in table for i in x]


if __name__ == "__main__":
    main()