# -*- coding: utf-8 -*-
"""
Created on Sat Jun 26 14:40:58 2021

@author: rodin
"""

def trapzint(f,a,b,n):
    
    h=(b-a)/n
    outputArg1=0
    
    for i in range(n):
        x_o=a+i*h
        x_1=a+(i+1)*h
        outputArg1+=(1/2)*h*(f(x_o)+f(x_1))
    
    return outputArg1

def trapzint2 (f,a,b,n):
    
    h=(b-a)/n
    
    outputArg1=(1/2)*h*(f(a)+f(b))
    
    for i in range(1,n):
        x=a+i*h
        outputArg1+=h*(f(x))
        
    return outputArg1

def test_trapzint():
    
    f= lambda x: 4*x+10
    
    exact=5500
    
    expct1=trapzint(f,0,50,10000)

    expct2=trapzint2(f,0,50,100000)
    
    success1=abs(exact-expct1)<1e-12
    
    success2=abs(exact-expct2)<1e-11
    
    msg1='test %d failed' %(1)
    
    msg2='test %d failed' %(2)
    
    assert success1, msg1
    assert success2, msg2

test_trapzint()

from numpy.lib.scimath import sqrt

f=lambda x: 1/(sqrt(4-x**2))

print(trapzint2(f, 0, 1, 1000000))