# -*- coding: utf-8 -*-
"""
Created on Mon Jun 28 17:12:31 2021

@author: rodin
"""

def piecewise(x,data):
    
    for i in range(len(data)-1):
        if x>=data[i][1] and x<data[i+1][1]:
            outputArg1=data[i][0]
        elif i==(len(data)-2) and x==data[len(data)-1][1]:
            outputArg1=data[i][0]
        
    return outputArg1



print(piecewise(1,[(-1,0),(0,1),(2,1.5),(4,2),(6,4)]))