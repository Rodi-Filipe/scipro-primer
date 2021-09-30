# -*- coding: utf-8 -*-
"""
Created on Mon Jun 28 16:52:46 2021

@author: rodin
"""
from math import pi, sin

def H_eps(x, eps=0.01):
    
    if x<-eps:
        outputArg1=0
    elif x>=-eps and x<=eps:
        outputArg1=0.5+x/(2*eps)+1/(2*pi)*sin((pi*x)/eps)
    elif x>eps:
        outputArg1=1
    
    return outputArg1

def test_H_eps():
    
    comp1=H_eps(-10)
    comp2=H_eps(-10**-15)
    comp3=H_eps(0)
    comp4=H_eps(10)
    
    assert abs(0-comp1)<1e-10
    assert abs(0.5-comp2)<1e-10
    assert abs(0.5-comp3)<1e-10
    assert abs(1-comp4)<1e-10

test_H_eps()