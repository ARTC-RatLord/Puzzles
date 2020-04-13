# -*- coding: utf-8 -*-
"""
Created on Sun Apr 12 14:59:05 2020

@author: 502598
"""

#Pig Latin to English
print('Enter the Pig Latin to translate to English message')
Pig_Latin=input()

Eng_message=[]

for word in Pig_Latin.split():
    suffix=''
    if not word[-1].isalpha():#if word is end with non-letter
        if word.isdecimal():
            continue
        else:
            suffix += word[-1]
            word=word[:-1]    
            
    wasUpper=word.isupper()
    wasTitle=word.istitle()
    
    word=word.lower()
    
    if word[len(word)-3:len(word)]=='yay':#if word is end with yay
        word=word[0:len(word)-3]
        
    
    if '-'in word:#if word contains'-'
        word_1=word.split('-')
        word_end=word_1[1]
        word2=word_end[0:len(word_end)-2]
        word=word2+word_1[0]
    
    if wasUpper:
        word = word.upper()
    if wasTitle:
        word = word.title()
        
    Eng_message.append(word+suffix)
print(' '.join(Eng_message))