# -*- coding: utf-8 -*-
"""
Created on Sun Jun 27 15:54:35 2021

@author: rodin
"""
from math import exp, e, cos, log as ln, pi

def diff(f,x,h=1E-5):
    
    outputArg1=(f(x+h)-f(x-h))/(2*h)
    
    return outputArg1

def test_diff():
    
    f=lambda x: e**(x)
    
    exact=2980.96
    
    expct=diff(f,h=1e-4,x=8)
    
    success=abs(exact-expct)<1e-2
    
    msg='test failed exact=%13.9f != to %13.9f \
(expected)' %(exact, expct)
        
    assert success, msg

def application():
    
    f1=lambda x: exp(x)
    f2=lambda x: exp(-2*x**2)
    f3=lambda x: cos(x)
    f4=lambda x: ln(x)
    tempvar=[[f1,0,1],[f2,0,0],[f3,2*pi,0],[f4,1,1]]
    
    print('     x            dydx    \
     error')
    print('----------------------------------------')
    for f, x, exact in tempvar:
        dxdy=diff(f,x,h=0.01)
        error=abs(exact-dxdy)
        print('%10.5f   %10.5f   %10.5f' \
              %(x,dxdy, error))
        
test_diff()

application()