# -*- coding: utf-8 -*-
"""
Created on Mon Jun 28 15:14:16 2021

@author: rodin
"""

def H(x):
    
    if x<0:
        outputArg1=0
    else:
        outputArg1=1
        
    return outputArg1

def test_H():
    
    comp1=H(-10)
    comp2=H(-10**-15)
    comp3=H(0)
    comp4=H(10)
    
    assert abs(0-comp1)<1e-10
    assert abs(0-comp2)<1e-10
    assert abs(1-comp3)<1e-10
    assert abs(1-comp4)<1e-10
    


test_H()

