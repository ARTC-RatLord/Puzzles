# -*- coding: utf-8 -*-
"""
Created on Fri Mar 20 21:01:25 2020

@author: 364970
"""
#random "balloons" some overlaop, some don't
x = [(114,136),(67,88),(14,126),(76,141),(66,78),(26,137),(85,133),(113,139),(43,141),(106,137),(60,128),(61,83),(57,102),
   (19,96),(43,99),(52,99),(41,102),(38,137),(71,108),(37,120)]
#the range were if we threw a dart it could hit something
hit_zone = range(min([balloon[0] for balloon in x]), max([balloon[1] for balloon in x]) +1)
 #converting the tuples in x to a list of ranges that will correspond to a hit
balloons = [range(balloon[0], balloon[1]+1) for balloon in x]
#function to return the location of a throw that would pop the most balloons
def find_max_pops(balloons):
    pops_total = []
    for throw in hit_zone:
        pops = []
        for balloon in balloons:
            if throw in balloon:
                pops.append('1')
        pops_total.append(len(pops))
    max_pops = max(pops_total)
    print(max_pops)
    return(pops_total.index(max_pops))
#function to throw the dart
def throw(x):
    new_balloons = []
    for b in balloons:
        if x not in b:
            new_balloons.append(b)
    return(new_balloons)
#loop to select and execute the best throw until there are no more balloons
while len(balloons) > 0:
    balloons = throw(find_max_pops(balloons))

    
