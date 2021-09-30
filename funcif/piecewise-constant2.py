# -*- coding: utf-8 -*-
"""
Created on Mon Jun 28 19:41:54 2021

@author: rodin
"""
def I(x,L,R):
    
    if x>=L and x<R:
        outputArg1=1
    else:
        outputArg1=0
        
    return outputArg1

def piecewise(x,data):
    
    outputArg1=0
    for i in range(len(data)-1):
        outputArg1+=data[i][0]*I(x,data[i][1],data[i+1][1])
        
        if i==(len(data)-2) and x==data[len(data)-1][1]:
            outputArg1=data[i][0]
    return outputArg1

    

print(piecewise(4,[(-1,0),(0.5,1),(2,1.5),(4,2),(6,4)]))