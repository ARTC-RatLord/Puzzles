# -*- coding: utf-8 -*-
"""
Created on Mon Mar 30 16:38:44 2020

@author: 502598
"""
#problem

#Background
#Find the smallest prime number greater than 2019 and can be formed as 4k+1(k is integer)
#Write it also as a sum square (x**2+y**2)


#Q1:What is the smallest prime number which can be represented as a sum of squares in 2 different ways?

'find prime number'
def is_prime(N):
    for i in range(2,round(N/2)+1):
        if N%i==0:
            return False
    if (N-1)%4==0:
        return i

prime=[]
for N in range(2019,3000):
    if is_prime(N):
        prime.append(N)
print(prime)
 
'find a sum square for prime'
def reps_sum_square(a):
        reps=[]
        for x in range(2, round((a/2)**.5)+1):
            if ((x**2)**.5)%1==0:#Question for Jake: can I use %1 to define a interger?
                y_square=a-x**2
                if (y_square**.5)%1==0:
                    y=int(y_square**.5)
                    reps.append((x,y))
        return reps

for a in prime:
    if reps_sum_square(a):
        len_reps=len(reps_sum_square(a))
        if len_reps >=2:
            print(a,':',reps_sum_square(a))
