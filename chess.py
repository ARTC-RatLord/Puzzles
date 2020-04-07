# -*- coding: utf-8 -*-
"""
Created on Mon Apr  6 11:32:20 2020

@author: 502598
"""
def ValidChessBoard(move):
    keys=list(move.keys())
    values=list(move.values())
    keys_number=keys[0]
    values_number=values[0]
    len_vn=len(values_number)
    print(values_number[1:len_vn])
    letter=['a','b','c','d','e','f','g','h']
    color=['w','b']
    chess=['pawn', 'knight', 'bishop', 'rook', 'queen','king']
    if int(keys_number[0]) in range(1,9):
        True
        if keys_number[1] in letter:
            True
            if values_number[0] in color:
                True
                if values_number[1:len_vn] in chess:
                    True
                    print('True')
                else:
                    print('False')
            else:
                print('False')
        else:
            print('False')
    else:
        return False
        print('False')
        
ValidChessBoard({'6c':'whappy'})



#Trying to add input
#move=input()
#if ValidChessBoard(move):
#    print(ValidChessBoard(move))
