# -*- coding: utf-8 -*-
"""
Created on Sat Jun 26 01:22:38 2021

@author: rodin
"""

def mysum(inputArg1):
    
    for i in range(len(inputArg1)):
        if i==0:
            runsum=inputArg1[i]
        elif i!=0:
            runsum+=inputArg1[i]
        
    return runsum

print(mysum([1,2,3,4,5,6]))
        
    
    