from game_functions import *

def minimax(position, depth, max_player, alpha, beta):
    if depth == 0 or check_win(1, board) == True or check_win(2, board) == True:
        return evaluate(position), position

    if max_player:
        maxEvaluation = -1000000000
        best_move = None
        moves = get_valid_moves(board)
        for move in moves:
            row = move[0]
            col = move[1]
            board[row][col] = 2
            evaluation = minimax(board, depth-1, False, alpha, beta)[0]
            maxEvaluation = max(maxEvaluation, evaluation)
            alpha = max(alpha, maxEvaluation)
            board[row][col] = 0
            if alpha >= beta:
                break
            if maxEvaluation == evaluation:
                best_move = move

        return maxEvaluation, best_move
    
    else:
        minEvaluation = 1000000000
        best_move = None
        moves = get_valid_moves(board)
        for move in moves:
            row = move[0]
            col = move[1]
            board[row][col] = 1
            evaluation = minimax(board, depth-1, True, alpha, beta)[0]
            minEvaluation = min(minEvaluation, evaluation)
            beta = min(beta, minEvaluation)
            board[row][col] = 0
            if alpha >= beta:
                break
            if minEvaluation == evaluation:
                best_move = move

        return minEvaluation, best_move