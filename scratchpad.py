import random

chess_pieces = {"pawn" : 0, "knight" : 1, "bishop" : 2, "queen" : 3, "king" : 4, "THE ROOOK!!!" : 5,}

def make_rank(size):
    rank = []
    for i in range(size):
        rank.append("[]")
    return rank

def make_board(size):
    board = []
    for papa in range(size):
        board.append(make_rank(size))
    return board

def show_board(board):
    size = len(board)
    for i in reversed(range(size)):
        print(i + 1, board[i])
    
board = make_board(8)
show_board(board)

letters = ["a", "b", "c", "d", "e", "f", "g", "h"]

def board_coordinates_for(square):
    letter = square[0]
    digit = square[1]
    return {"rank": int(digit) - 1, "file": letters.index(letter)}

print(board_coordinates_for("d5"))
