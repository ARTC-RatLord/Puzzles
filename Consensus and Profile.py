# -*- coding: utf-8 -*-
"""
Created on Sun May 17 15:37:38 2020

@author: 502598
"""
import re

file1=open(r"C:\Users\502598\Documents\Python\rosalind_cons (12).txt")
strings=file1.read()
print(strings)
#strings='''>Rosalind_1
#ATCCAGCT
#>Rosalind_2
#GGGCAACT
#>Rosalind_3
#ATGGATCT
#>Rosalind_4
#AAGCAACC
#>Rosalind_5
#TTGGAACT
#>Rosalind_6
#ATGCCATT
#>Rosalind_7
#ATGGCACT'''
strings=strings.replace('\n','')

unit=re.compile(r'>Rosalind_\d\w+')
DNA=unit.findall(strings)
print(DNA)
print(len(DNA[0]))
profile=[]
#title='>Rosalind_1'
#len_DNA=len(DNA[0])-len(title)
for n in range(14,len(DNA[0])):
        a=[]
        for i in range(0,len(DNA)):
            a.append(DNA[i][n])
        profile.append(a)
#print(profile)
print(len(profile))
A=''
C=''
G=''
T=''
consesus=''
for i in profile:
    con={}
    A+=str(i.count('A'))
    C+=str(i.count('C'))
    G+=str(i.count('G'))
    T+=str(i.count('T'))
    con['A']=i.count('A')
    con['C']=i.count('C')
    con['G']=i.count('G')
    con['T']=i.count('T')
    #print(con)
    for k,v in con.items():
        if v==max(con.values()):
            #print(k)
            consesus+=k
A=" ".join(A)
C=" ".join(C)
G=" ".join(G)
T=" ".join(T)
print(consesus)
print('A: '+ A)
print('C: '+ C)
print('G: '+ G)
print('T: '+ T)
print(len(A))   
    