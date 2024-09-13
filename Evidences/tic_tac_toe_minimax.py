import sys
import numpy as np
import random
player_value_to_display = {-1:'O',1:'X',0:' '}
class tic_tac_toe_game:
    def __init__(self,game_type=0):
        self.board = np.zeros((3,3),dtype=int)
        self.finished = False
        self.display_game_state()
        self.current_move = 1

        if game_type == 0:
            while not self.finished:
                player = self.current_move
                #moves = self.get_possible_moves()
                #print(moves)
                #row = list(moves.keys())[0]
                if self.current_move == -1:
                    deciding = True
                    while deciding:
                        row = int(input("select row!:"))
                        col = int(input("select column!:"))
                        if self.board[row][col] == 0:

                            self.make_move(player,row,col)
                            deciding = False
                else:
                    self.minimax_best_choice()
                pass

        pass
    def reset_game(self):
        self.board = np.zeros((3, 3), dtype=int)
        self.display_game_state()
    def make_move(self,player,row,column):
        if self.check_move_available(row,column):
            self.board[row][column] = player
            if self.check_win(player):
                print(f'{player_value_to_display[player]} Won')
                self.finished = True
                self.display_game_state()
            elif self.check_full_board():
                print('Draw!')
                self.finished = True
                self.display_game_state()
            else:
                self.current_move *= -1
                self.display_game_state()

    def check_win(self,player):
            for column in range(3):
                if (self.board[0][column] + self.board[1][column] + self.board[2][column]) == player * 3:
                    return True
            for row in range(3):
                if (self.board[row][0] + self.board[row][1] + self.board[row][2]) == player * 3:
                    return True
            if (self.board[0][0] + self.board[1][1] + self.board[2][2]) == player * 3:
                return True
            elif (self.board[0][2] + self.board[1][1] + self.board[2][0]) == player * 3:
                return True
            return False
    def check_full_board(self):
        for row in range(3):
            for column in range(3):
                if self.board[row][column] == 0:
                    return False
        return True
    def check_empty_board(self):
        for row in range(3):
            for column in range(3):
                if self.board[row][column] != 0:
                    return False
        return True
    def minimax(self,deep,maximizer):
        if self.check_win(1):
            return float('inf')
        elif self.check_win(-1):
            return float('-inf')
        elif self.check_full_board():
            return 0

        if maximizer:
            max_score = -1000
            for row in range(3):
                for column in range(3):
                    if self.board[row][column] == 0:
                        self.board[row][column] = 1
                        score = self.minimax(deep+1,False)
                        self.board[row][column] = 0
                        max_score = max(score,max_score)
            return max_score
        else:
            max_score = 1000
            for row in range(3):
                for column in range(3):
                    if self.board[row][column] == 0:
                        self.board[row][column] = -1
                        score = self.minimax(deep + 1, True)
                        self.board[row][column] = 0
                        max_score = min(score, max_score)
            return max_score
        pass
    def minimax_best_choice(self):
        if self.check_empty_board():
            self.make_move(1, 0, 0)
            return
        best_score = -1000
        move = (-1,-1)
        for row in range(3):
            for column in range(3):
                if self.board[row][column] == 0:
                    self.board[row][column] = 1
                    score = self.minimax(0, False)
                    self.board[row][column] = 0
                    if score > best_score:
                        best_score = score
                        move = (row,column)
        if move != (-1,-1):
            self.make_move(1,move[0],move[1])
            print("best move - ",move)
    def get_possible_moves(self):
        moves = {}
        for row in range(3):
            for column in range(3):
                if self.board[row][column] == 0:
                    if not row in moves:
                        moves[row] = []
                    moves[row].append(column)
        #print(moves)
        return moves

    def check_move_available(self,row,column):
        #print(f"Row: {row}, Column: {column}")
        return self.board[row][column] == 0

    def display_game_state(self):
        pvtd = player_value_to_display
        print("Game State:")
        print(f' {pvtd[self.board[0][0]]} |{pvtd[self.board[0][1]]} |{pvtd[self.board[0][2]]} \n'
              f' {pvtd[self.board[1][0]]} |{pvtd[self.board[1][1]]} |{pvtd[self.board[1][2]]} \n'
              f' {pvtd[self.board[2][0]]} |{pvtd[self.board[2][1]]} |{pvtd[self.board[2][2]]} ')
        #print(self.board)
game = tic_tac_toe_game()