# -*- coding: utf-8 -*-
"""
Created on Wed Apr 29 08:59:20 2020

@author: 502598
"""



print('please input the key from letters without space')

key=input()

print('please choose the mode encrypt or decrypt')

mode=input()
if mode !='encrypt' and mode != 'decrypt':
    print('please choose the mode encrypt or decrypt')
    mode=input()

print('please enter the message')

message=input()

symbol= 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'

#Convert key_letter into index
key_index=[]
for i in key:
    if i.islower():
       i=i.upper()
    letter_index=symbol.find(i)
    key_index.append(letter_index)
#print(key_index)

translate=''
for i in range(0,len(message)):
    if message[i].isalpha():
        n=message[i]
        wasLower=n.islower()
        n=n.upper()
        n_index=symbol.find(n)
        #print(n_index)
        l_index=i%len(key)
        #print(l_index,'end')
        if mode=='encrypt':
            n_index=n_index+key_index[l_index]
            n_index=n_index%26
        if mode=='decrypt':
            n_index=n_index-key_index[l_index]
            if n_index<0:
                n_index=26+n_index
            #print(n_index)
        n=symbol[n_index]
        if wasLower:
            n=n.lower()
        translate +=n
    else:
        translate += message[i]
print(translate + ' Key=' +key)

                
                
        
            
    


           

