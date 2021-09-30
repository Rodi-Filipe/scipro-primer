# -*- coding: utf-8 -*-
"""
Created on Thu Jul  1 20:30:48 2021

@author: rodin
"""

from math import exp, sin 

def expsin(x, p, q): 
    return exp(p*x)*sin(q*x)
def f(x, m, n, r, s): 
    return expsin(x, r, m) + expsin(x, s, n) 

x = 2.5 
print(f(x, 0.1, 0.2, 1, 1))
