# -*- coding: utf-8 -*-
"""
Created on Sat Jun 26 20:16:50 2021

@author: rodin
"""

def func0(a,b,f,n):
    
    outputArg1=[a+i*(b/n) for i in range(n)]
    outputArg2=[f(outputArg1[i]) \
                for i in range(len(outputArg1))]
    
    return outputArg1,outputArg2
    

def pathlength(x,y):
    
    from math import sqrt
    L=0
    for i in range(1,len(x)):
        L+=sqrt((x[i]-x[i-1])**2+(y[i]-y[i-1])**2)
        
    print(L)
    return L

def test_pathlength():
    
    from math import pi, sin
    f=lambda x: sin(x)**2
    
    exact=3.82019778902771
    
    x, y=func0(0,pi,f,1000000)
    expct=pathlength(x,y)
    
    success=abs(exact-expct)<1e-10
    
    msg='test failed,  exact=%5.2f != to %5.2f (expected)' \
        %(exact, expct)
        
    assert success, msg

test_pathlength()