# -*- coding: utf-8 -*-
"""
Created on Mon Jun 28 14:29:37 2021

@author: rodin
"""

from math import cos, pi, sqrt

def maxmin(f,a,b,n=1000):
    
    h=((b-a)/n)
    x=[a+i*h for i in range(n)]
    y=[f(i) for i in x]
    
    return max(y), min(y)


def test_maxmin():
    
    minvar=-1
    maxvar=1
    
    expct1, expct2=maxmin(cos,-pi/2,2*pi)
    
    assert abs(expct1-maxvar)<1e-3
    assert abs(expct2-minvar)<1e-3
    

test_maxmin()

f=lambda x: sqrt(1+x**2)
maxvar, minvar=maxmin(f,0,20.5)

print('%9.4f %9.4f' %(maxvar,minvar))