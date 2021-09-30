# -*- coding: utf-8 -*-
"""
Created on Sun Jun 27 15:54:35 2021

@author: rodin
"""
from math import exp, e

def diff(f,x,h=1E-5):
    
    outputArg1=(f(x+h)-f(x-h))/(2*h)
    
    return outputArg1

def test_diff():
    
    f=lambda x: e**(x)
    
    exact=2980.96
    
    expct=diff(f,h=1e-10,x=8)
    
    success=abs(exact-expct)<1e-3
    
    msg='test failed exact=%13.9f != to %13.9f \
(expected)' %(exact, expct)
        
    assert success, msg


print(diff(exp,7))