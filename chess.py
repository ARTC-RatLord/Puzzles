# -*- coding: utf-8 -*-

def ValidChessBoard(move):
    valid_pieces = ['pawn', 'bishop', 'king', 'queen', 'knight', 'rook']
    valid_letters = ['a','b','c','d','e','f','g','h']
    valid_colors = ['w', 'b']
    square_flag = True
    for square in move.keys():
        if int(square[0]) not in range(1,9) or square[1] not in valid_letters:
            square_flag = False
    piece_flag = True
    for piece in move.values():
        if piece[0] not in valid_colors or piece[1:] not in valid_pieces:
            piece_flag = False
        
    if square_flag and piece_flag == True:
       return('VALID')
    else:
        return('NOT VALID')


board = {'1h': 'bking', '4c':'wqueen', '2g':'bbishop', '5h':'bqueen', '3e':'wking'}

print('what piece do you want to move')
piece = input()
print('where to?')
square = input()
board[square] = piece
print(str(board) + ' IS ' + ValidChessBoard(board))
