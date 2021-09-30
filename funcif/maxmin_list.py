# -*- coding: utf-8 -*-
"""
Created on Mon Jun 28 14:45:24 2021

@author: rodin
"""

import random 

def mymax(inputArg1):
    
    max_elem=inputArg1[0]
    
    for i in range(len(inputArg1)):
        for j in inputArg1[i+1:]:
            if max_elem<j:
                max_elem=j
    
    return max_elem

def mymin(inputArg1):
    
    min_elem=inputArg1[0]
    
    for i in range(len(inputArg1)):
        for j in inputArg1[i+1:]:
            if min_elem>j:
                min_elem=j
    
    return min_elem

a=random.sample(range(91),40)

print(a,end='\n\n')
print(mymax(a))
print(max(a))
print(mymin(a))
print(min(a))