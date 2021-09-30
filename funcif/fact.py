# -*- coding: utf-8 -*-
"""
Created on Mon Jun 28 01:00:43 2021

@author: rodin
"""

def fact(n):
    
    #n=eval(input('Please insert a value for n:\n>> '))
    outputArg1=1
    if n==0:
        outputArg1=1
    else:
        for i in range(n,0,-1):
            outputArg1*=i
        
    return outputArg1

def test_fact(): 
    # Check an arbitrary case 
    n = 4 
    expected = 4*3*2*1 
    computed = fact(n) 
    assert computed == expected 
    # Check the special cases 
    assert fact(0) == 1 
    assert fact(1) == 1


test_fact()

print(fact(1))