# -*- coding: utf-8 -*-
"""
Created on Wed Apr 29 08:59:20 2020

@author: 502598
"""



print('please input the key between 0 to 26')

key=int(input())

print('please choose the mode encrypt or decrypt')

mode=input()
if mode !='encrypt' and mode != 'decrypt':
    print('please choose the mode encrypt or decrypt')
    mode=input()

print('please enter the message')

message=input()

symbol= 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
translate=''

for n in message:
    if n.isalpha():
        wasLower=n.islower()
        n=n.upper()
        n_index=symbol.find(n)
        if mode=='encrypt':
            n_index=n_index+key
            if n_index>26:
                n_index=n_index-26
        if mode=='decrypt':
            n_index=n_index-key
            if n_index<0:
                n_index=26+n_index
        n=symbol[n_index]
        if wasLower:
            n=n.lower()
        translate +=n
    else:
        translate +=n
print(translate + ' KEY='+ str(key))

                
                
        
            
    


           

