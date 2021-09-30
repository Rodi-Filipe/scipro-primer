# -*- coding: utf-8 -*-
"""
Created on Sat Jun 26 16:27:06 2021

@author: rodin
"""

def midpointint(f,a,b,n):
    
    h=(b-a)/n
    outputArg1=0
    
    for i in range(0,n):
        x=a+i*h+0.5*h
        outputArg1+=h*f(x)
        
    return outputArg1

def trapzint2 (f,a,b,n):
    
    h=(b-a)/n
    
    outputArg1=(1/2)*h*(f(a)+f(b))
    
    for i in range(1,n):
        x=a+i*h
        outputArg1+=h*(f(x))
        
    return outputArg1


from math import sin, cos, pi

print(midpointint(lambda x: 2*x, 2, 4, 10000000))

print(trapzint2(lambda x: 2*x, 2, 4, 1000000))

