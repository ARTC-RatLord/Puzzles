# -*- coding: utf-8 -*-
"""
Created on Wed May  6 10:47:11 2020

@author: 502598
"""

DNA='''atcggtcggcgcctgttcaggcatgagctaagacaactccagtgaacgcgtgaagtgtcc
gggtgcaggcgttacctggagctagcaaaaggccacacaccagatctgtctttccatttt
aatctataggatttaagtcgtcttagccctgaagcatccttccaggcccccctcatgcgg
gccatctagctatctctaatgcctcatccacatactacacaaagtaaattagcatattct
tacgtggtcccgtcgcggtgcctaacgcgttgcttaatccacacgcgagtcgacgtcctc
cgttgccgtgaccgtccacagaggccatcctggggaacgttgaccaatccagtcgcccag
tgcttaccagttgaagatattagttctgtagaactaaaatagtcatgccaaactgacggc
ctgcagttaaccgtacgcgttgagcataatacactgaaccaccgtttgagcttccccacg
attagtacacgacctattcttctccacgaacggtacaggtatagtggatgagtccgagac
actcaaacggtgagcaatcgacggcatcgagcctccagcatacgagcactatattcatgg
tgcacatagtatgtcataccaagagtgatattccgacaagttgctgtgtcgctctacgac
gatattcacatatacataatctccggggagcatcttgtacgagagggtaattggtgagta
ttcccatgcccctactataatatcaagacggccgaatggcctatcggtaagtgtattaat
tgaaatgactatcacctgagcccttcgacaccctgcctgtaacagcttaaacatacgctt
caatttgtagcgtgctccattaagcgctccgccctgtgctgcacttctgaaccataggcc
cggcatgctacgcgcggatcaatggcacaagagtcttgcagataattcacaactacaggc
tgtagagagggcgtccattctacccctagcaaccgtgttg'''

pattern='atc'

m=len(DNA) # for mod
n=len(pattern) #for evaluation number

h_p=0 # initial hash value of pattern
h_DNA=0 #initial hash value of DNA

result=0

for i in range(0,n):
    h_p +=ord(pattern[i])*n**i
    #print(h_p)
h_p_mod=h_p%m #hash value with mod of pattern  
print(h_p_mod)

for i in range(0,n):
    h_DNA +=ord(DNA[i])*(n**i)
    #print(h_DNA)
h_DNA_mod=h_DNA%m #first hash value in DNA sequence
print(h_DNA_mod)
#
if h_p_mod==h_DNA_mod: # if the first time search is match
    result +=1
    print('position: '+ '0')
    
for i in range(1, m-n+1):
    h_DNA= (h_DNA-ord(DNA[i-1]))/n+ord(DNA[i+n-1])*n**(n-1)
    h_DNA_mod=h_DNA%m
    #print(h_DNA_mod)
    if h_DNA_mod == h_p_mod: #found out the same hash value and comparing the letter
        j=0
        if DNA[i]==pattern[j]:
                j+=1
        result+=1
        print('position: '+ str(i))
        
print('Total result: ' + str(result))
    
    
