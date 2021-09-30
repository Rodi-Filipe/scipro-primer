# -*- coding: utf-8 -*-
"""
Created on Sat Aug 21 02:37:36 2021

@author: rodin
"""

import numpy as np
from math import exp

def f(A):
    
    if isinstance(A, np.ndarray):
        outputArg1=[ [ x**3+x*exp(x)+1 for x in A[k,:]] for k in range(A.shape[0]) ]
    
    return np.array(outputArg1)

def prog1():
    
    A=np.array([[0,2,-1],[-1,-1,0],[0,5,0]])
    
    print(f(A),'\n')
    
    print(A**3+A*np.exp(A)+1,'\n')
    
    print(abs(f(A)-(A**3+A*np.exp(A)+1)))
    
prog1()