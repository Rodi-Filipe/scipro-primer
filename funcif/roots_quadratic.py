# -*- coding: utf-8 -*-
"""
Created on Sat Jun 26 00:48:17 2021

@author: rodin
"""

def roots_quadratic(a, b, c):
     
    from numpy.lib.scimath import sqrt
     
    x1=(-b+sqrt(b**2-4*a*c))/(2*a)
     
    x2=(-b-sqrt(b**2-4*a*c))/(2*a)
     
    return x1, x2



def test_roots_float():
    
    x1=-0.2
    
    x2=-1
    
    expx1, expx2=roots_quadratic(5,6,1)
    
    result1=(x1==expx1)
    
    result2=(x2==expx2)
    
    msg1='test %d failed' %(1)
    
    msg2='test %d failed' %(2)
    
    assert result1, msg1
    
    assert result2, msg2

def test_roots_complex():
    
    x1=-0.2+0.4j
    
    x2=-0.2-0.4j
    
    expx1, expx2=roots_quadratic(5,2,1)
    
    result1=(x1==expx1)
    
    result2=(x2==expx2)
    
    msg1='test %d failed' %(3)
    
    msg2='test %d failed' %(4)
    
    assert result1, msg1
    
    assert result2, msg2


test_roots_float()

test_roots_complex()
     