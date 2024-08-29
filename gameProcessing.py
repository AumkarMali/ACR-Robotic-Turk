import chess, random
import time
import numpy as np
#from ServoControl import move_arm, piece_remove
from art import tprint
import json

#Program introduction
tprint("Welcome   to   ACR")

board = chess.Board()
programMoveCtr = 0

#Algorithm Presets: will change behavior of program
depth = 4 #Number of future turn predictions made
timedKingDefensiveVal = 0.05 #Increases program bias toward defending king after n moves


def evaluate(board, programColor, programMoveCtr):
    whiteScore, blackScore = 0, 0

    def getKingDefenceScore(board, programMoveCtr):
        bScore, wScore = 0, 0

        scores = {
            'p': 1,
            'n': 2,
            'b': 3,
            'r': 4,
            'q': 5
        }

        strBoard = list(str(board))
        arr = list(filter(lambda x: x != ' ' and x != '\n', strBoard))

        matrixBoard = [arr[i:i + 8] for i in range(0, 64, 8)]
        npMatrixBoard = np.asarray(matrixBoard)
        blackKingPos, whiteKingPos = np.argwhere(npMatrixBoard == 'k'), np.argwhere(npMatrixBoard == 'K')

        # check surrounding pieces of king both black and white
        def sp(row, col, npMatrixBoard):
            pieces = []
            for dr in [-1, 0, 1]:
                for dc in [-1, 0, 1]:
                    if dr == 0 and dc == 0:
                        continue
                    new_row, new_col = row + dr, col + dc
                    if 0 <= new_row < 8 and 0 <= new_col < 8:
                        pieces.append(str(npMatrixBoard[new_row, new_col]))
            return pieces

        spWhite = sp(whiteKingPos[0][0], whiteKingPos[0][1], npMatrixBoard)
        spBlack = sp(blackKingPos[0][0], blackKingPos[0][1], npMatrixBoard)

        for p in spWhite:
            if p.lower() in scores.keys():
                wScore += scores[p.lower()]
        for p in spBlack:
            if p.lower() in scores.keys():
                bScore += scores[p.lower()]

        return round((1 / 5) * (wScore ** 2) * programMoveCtr), round((1 / 5) * (bScore ** 2) * programMoveCtr)


    #Scoring based on number of chess pieces
    for c in str(board):
        if c == 'p':
            blackScore += 10
        elif c == 'r':
            blackScore += 50
        elif c == 'n' or c == 'b':
            blackScore += 30
        elif c == 'q':
            blackScore += 90
        elif c == 'P':
            whiteScore += 10
        elif c == 'R':
            whiteScore += 50
        elif c == 'N' or c == 'B':
            whiteScore += 30
        elif c == 'Q':
            whiteScore += 90

    #king safety analysis
    w, b = getKingDefenceScore(board, programMoveCtr)
    whiteScore += w
    blackScore += b

    if programColor == 'white':
        return whiteScore - blackScore
    else:
        return blackScore - whiteScore


def minimax(board, depth, alpha, beta, maxPlayer, programColor, programMoveCtr):
    global instanceCTR
    instanceCTR += 1

    if depth == 0 or board.is_game_over():
        return evaluate(board, programColor, programMoveCtr), None

    moves = list(board.generate_legal_moves())
    best_move = random.choice(moves) if moves else None

    if maxPlayer:
        maxEval = float('-inf')

        for m in moves:
            board.push(m) #indicates to the chess library next players turn
            curEval, _ = minimax(board, depth - 1, alpha, beta, False, programColor, programMoveCtr)
            board.pop()

            if curEval > maxEval:
                maxEval = curEval
                best_move = m

            alpha = max(alpha, curEval)
            if beta <= alpha:
                break
        return maxEval, best_move
    else:
        minEval = float('inf')

        for m in moves:
            board.push(m)
            curEval, _ = minimax(board, depth - 1, alpha, beta, True, programColor, programMoveCtr)
            board.pop()

            #lowest score on eval function yields optimal move for minimizing player
            if curEval < minEval:
                minEval = curEval
                best_move = m

            beta = min(beta, curEval)
            if beta <= alpha:
                break

        return minEval, best_move


while not board.is_game_over():
    # indicates whether human/computer gets the first turn
    if board.turn == chess.WHITE:
        with open('save_move.txt', 'r') as file:
            fl = file.readline().strip()

        move = fl
        if move:
            try:
                #checks square for existing pieces
                checkSqInp = chess.parse_square(move[2] + move[3])
                pieceExistEnemy = board.piece_at(checkSqInp)
                board.push_uci(move)

                if pieceExistEnemy:
                    continue
                    #piece_remove(move, False)
                    #move_arm(move)
                else:
                    continue
                    #move_arm(move)
            except:
                continue

    else:
        instanceCTR = 0
        startTimer = time.perf_counter()
        print()
        print(f"Program analysing next {depth} moves...")

        _, best_move = minimax(board, depth, float('-inf'), float('inf'), False, 'white', programMoveCtr)
        strBestMove = str(best_move)

        if best_move:
            stopTimer = time.perf_counter()
            programMoveCtr += timedKingDefensiveVal

            print(f"Engine plays: {best_move}; Number of Instances: {instanceCTR}; time taken: {stopTimer - startTimer:0.2f} sec; Ctr: {round(programMoveCtr, 2)}")
            
            checkSqInpProg = chess.parse_square(strBestMove[2] + strBestMove[3])
            pieceExistPlayer = board.piece_at(checkSqInpProg)
            board.push(best_move)

            with open('save_move.txt', 'a') as f:
                f.write(str(best_move) + '\n')
            
            if pieceExistPlayer:
                continue
                #piece_remove_move(str(best_move), True)
                #move_arm(str(best_move))
            else:
                continue
                #move_arm(str(best_move))


print("Game over")
print("Result:", board.result())