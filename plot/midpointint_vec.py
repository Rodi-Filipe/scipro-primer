# -*- coding: utf-8 -*-
"""
Created on Mon Jul 19 01:25:59 2021

@author: rodin
"""

import numpy as np

def midpointint(f,a,b,n):
    
    h=(b-a)/n
    outputArg1=0
    
    for i in range(0,n):
        x=a+i*h+0.5*h
        outputArg1+=h*f(x)
        
    return outputArg1

def midpointint_v1(f,a,b,n):
    
    h=(b-a)/n
    x=np.linspace(a+0.5*h,b-0.5*h,n)
    y=f(x)
    outputArg1=h*sum(y)
    
    return outputArg1

def midpointint_v2(f,a,b,n):
    
    h=(b-a)/n
    x=np.linspace(a+0.5*h,b-0.5*h,n)
    y=f(x)
    outputArg1=h*np.sum(y)
    
    return outputArg1

def test_midpoint():
    
    f=lambda x: 2*x
    a=2
    b=4
    n=100
    exact=12
    expected=midpointint(f,a,b,n)
    
    assert exact==expected, 'test failed! %4.1f != %4.1f' %(exact, expected)
    
def test_midpoint_v1():
    
    f=lambda x: 2*x
    a=2
    b=4
    n=100
    exact=12
    expected=midpointint_v1(f,a,b,n)
    
    assert exact==expected, 'test failed! %4.1f != %4.1f' %(exact, expected)

def test_midpointint_v2():
    
    f=lambda x: 2*x
    a=2
    b=4
    n=100
    exact=12
    expected=midpointint_v2(f,a,b,n)
    
    assert exact==expected, 'test failed! %4.1f != %4.1f' %(exact, expected)
    
if __name__ == '__main__':
    
    test_midpoint()
    
    test_midpoint_v1()
    
    test_midpointint_v2()
    
__all__ = ['midpointint', 'midpointint_v1', 'midpointint_v2']