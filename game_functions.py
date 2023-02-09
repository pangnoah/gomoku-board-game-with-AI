import pygame
import numpy as np
from constants import *

board = np.zeros((ROWS, COLS))
SCREEN = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT))

def mark_square(row, col, player):
    board[row][col] = player

def unmark_square(row, col):
    board[row][col] = 0

def available_square(row, col):
    if row > 0 and col > 0:
        return board[row][col] == 0

def draw_figures():
    for row in range(ROWS):
        for col in range(COLS):
            if board[row][col] == 1:
                pygame.draw.circle(SCREEN, BLACK, (int(col*BLOCK_SIZE), int(row*BLOCK_SIZE)), 18)
            elif board[row][col] == 2:
                pygame.draw.circle(SCREEN, WHITE, (int(col*BLOCK_SIZE), int(row*BLOCK_SIZE)), 18)

def check_win(player, board):
    for col in range(COLS):
        for row in range(ROWS):
            if (col < 12 and board[row][col] == player
            and board[row][col+1] == player
            and board[row][col+2] == player
            and board[row][col+3] == player
            and board[row][col+4] == player):
                return True

            if (row < 12 and board[row][col] == player
            and board[row+1][col] == player
            and board[row+2][col] == player
            and board[row+3][col] == player
            and board[row+4][col] == player):
                return True

            if (row > 4 and col < 12 and board[row][col] == player 
            and board[row-1][col+1] == player 
            and board[row-2][col+2] == player 
            and board[row-3][col+3] == player
            and board[row-4][col+4] == player):
                return True

            if (row < 12 and col < 12 and board[row][col] == player 
            and board[row+1][col+1] == player 
            and board[row+2][col+2] == player 
            and board[row+3][col+3] == player
            and board[row+4][col+4] == player):
                return True

    return False

def draw_grid():
    for x in range(0, WINDOW_WIDTH, BLOCK_SIZE):
        for y in range(0, WINDOW_HEIGHT, BLOCK_SIZE):
            rect = pygame.Rect(x, y, BLOCK_SIZE, BLOCK_SIZE)
            pygame.draw.rect(SCREEN, BLACK, rect, 1)

def restart():
    SCREEN.fill(BROWN)
    draw_grid()
    for row in range(ROWS):
        for col in range(COLS):
            board[row][col] = 0

def evaluate(board):
    board
    if check_win(1, board):
        return -1000000
    if check_win(2, board):
        return 1000000
    
    return score(2, board) - score(1, board)

def get_valid_moves(board):
    moves = []
    for row in range(ROWS):
        for col in range(COLS):
            if row > 0 and col > 0 and board[row][col] != 0:
                if row < 15 and tuple((row+1, col)) not in moves and board[row+1][col] == 0:
                    moves.append(tuple((row+1,col)))
                
                if row < 15 and col < 15 and tuple((row+1, col+1)) not in moves and board[row+1][col+1] == 0:
                    moves.append(tuple((row+1,col+1)))

                if row < 15 and col > 1 and tuple((row+1, col-1)) not in moves and board[row+1][col-1] == 0:
                    moves.append(tuple((row+1,col-1)))

                if col < 15 and tuple((row, col+1)) not in moves and board[row][col+1] == 0:
                    moves.append(tuple((row,col+1)))

                if col > 1 and tuple((row, col-1)) not in moves and board[row][col-1] == 0:
                    moves.append(tuple((row,col-1)))

                if row > 1 and col < 15 and tuple((row-1, col+1)) not in moves and board[row-1][col+1] == 0:
                    moves.append(tuple((row-1,col+1)))

                if row > 1 and tuple((row-1, col)) not in moves and board[row-1][col] == 0:
                    moves.append(tuple((row-1,col)))

                if row > 1 and col > 1 and tuple((row-1, col-1)) not in moves and board[row-1][col-1] == 0:
                    moves.append(tuple((row-1,col-1)))
                
    return moves

def score(p, board):
    sum = 0
    list = []
    opp = p % 2 + 1
    for col in range(1, COLS):
        for row in range(1, ROWS):
            x = board[row][col]
            list.append(x)
    indices = [i for i, x in enumerate(list) if x == 1 or x == 2]
    for i in indices:
        if i < 224 and list[i] == p and list[i+1] == p:
            sum+=1
        if i < 211 and list[i] == p and list[i+14] == p:
            sum+=1
        if i < 210 and list[i] == p and list[i+15] == p:
            sum+=1
        if i < 209 and list[i] == p and list[i+16] == p:
            sum+=1
        if i < 223 and list[i] == p and list[i+1] == p and list[i+2] == p:
            sum+=20
        if i < 197 and list[i] == p and list[i+14] == p and list[i+28] == p:
            sum+=20
        if i < 195 and list[i] == p and list[i+15] == p and list[i+30] == p:
            sum+=20
        if i < 193 and list[i] == p and list[i+16] == p and list[i+32] == p:
            sum+=20
        if i < 222 and list[i] == opp and list[i+1] == opp and list[i+2] == p and list[i+3] == opp:
            sum+=300
        if i < 222 and list[i] == opp and list[i+1] == p and list[i+2] == opp and list[i+3] == opp:
            sum+=300
        if i < 183 and list[i] == opp and list[i+14] == opp and list[i+28] == p and list[i+42] == opp:
            sum+=300
        if i < 183 and list[i] == opp and list[i+14] == p and list[i+28] == opp and list[i+42] == opp:
            sum+=300
        if i < 180 and list[i] == opp and list[i+15] == opp and list[i+30] == p and list[i+45] == opp:
            sum+=300
        if i < 180 and list[i] == opp and list[i+15] == p and list[i+30] == opp and list[i+45] == opp:
            sum+=300
        if i < 177 and list[i] == opp and list[i+16] == opp and list[i+32] == p and list[i+48] == opp:
            sum+=300
        if i < 177 and list[i] == opp and list[i+16] == p and list[i+32] == opp and list[i+48] == opp:
            sum+=300
        if i < 221 and list[i] == p and list[i+1] == opp and list[i+2] == opp and list[i+3] == opp and list[i+4] == 0:
            sum+=1000
        if i < 169 and list[i] == p and list[i+14] == opp and list[i+28] == opp and list[i+42] == opp and list[i+56] == 0:
            sum+=1000
        if i < 165 and list[i] == p and list[i+15] == opp and list[i+30] == opp and list[i+45] == opp and list[i+60] == 0:
            sum+=1000
        if i < 161 and list[i] == p and list[i+16] == opp and list[i+32] == opp and list[i+48] == opp and list[i+64] == 0:
            sum+=1000
        if i > 3 and list[i] == p and list[i-1] == opp and list[i-2] == opp and list[i-3] == opp and list[i-4] == 0:
            sum+=1000
        if i > 55 and list[i] == p and list[i-14] == opp and list[i-28] == opp and list[i-42] == opp and list[i-56] == 0:
            sum+=1000
        if i > 59 and list[i] == p and list[i-15] == opp and list[i-30] == opp and list[i-45] == opp and list[i-60] == 0:
            sum+=1000
        if i > 63 and list[i] == p and list[i-16] == opp and list[i-32] == opp and list[i-48] == opp and list[i-64] == 0:
            sum+=1000
        if i < 222 and list[i] == p and list[i+1] == p and list[i+2] == p and list[i+3] == p:
            sum+=5000
        if i < 183 and list[i] == p and list[i+14] == p and list[i+28] == p and list[i+42] == p:
            sum+=5000
        if i < 180 and list[i] == p and list[i+15] == p and list[i+30] == p and list[i+45] == p:
            sum+=5000
        if i < 177 and list[i] == p and list[i+16] == p and list[i+32] == p and list[i+48] == p:
            sum+=5000
        if i < 221 and list[i] == opp and list[i+1] == opp and list[i+2] == opp and list[i+3] == opp and list[i+4] == p:
            sum+=50000
        if i < 169 and list[i] == opp and list[i+14] == opp and list[i+28] == opp and list[i+42] == opp and list[i+56] == p:
            sum+=50000
        if i < 165 and list[i] == opp and list[i+15] == opp and list[i+30] == opp and list[i+45] == opp and list[i+60] == p:
            sum+=50000
        if i < 161 and list[i] == opp and list[i+16] == opp and list[i+32] == opp and list[i+48] == opp and list[i+64] == p:
            sum+=50000
        if i < 221 and list[i] == p and list[i+1] == opp and list[i+2] == opp and list[i+3] == opp and list[i+4] == opp:
            sum+=50000
        if i < 169 and list[i] == p and list[i+14] == opp and list[i+28] == opp and list[i+42] == opp and list[i+56] == opp:
            sum+=50000
        if i < 165 and list[i] == p and list[i+15] == opp and list[i+30] == opp and list[i+45] == opp and list[i+60] == opp:
            sum+=50000
        if i < 161 and list[i] == p and list[i+16] == opp and list[i+32] == opp and list[i+48] == opp and list[i+64] == opp:
            sum+=50000

    return sum