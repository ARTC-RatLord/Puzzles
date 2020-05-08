# -*- coding: utf-8 -*-
"""
Created on Thu May  7 13:43:58 2020

@author: 502598
"""

def mortal_fib(n,m):

    mfib=[1,1] 
    for i in range(2,m+1):
        mfib_i=mfib[i-2]+mfib[i-1]
        mfib.append(mfib_i)
        #print(mfib)
    mfib[m]=mfib[m]-1#rule out the first death of rabbit
    
        
    for i in range(m+1,n):
        mfib_i=mfib[i-1]+mfib[i-2]-mfib[i-1-m] # adding death to fibonacci
        mfib.append(mfib_i)
        #print(mfib)
    print(mfib[-1])

mortal_fib(6,3)

