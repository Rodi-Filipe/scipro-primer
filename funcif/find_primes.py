# -*- coding: utf-8 -*-
"""
Created on Thu Jul  1 18:01:08 2021

@author: rodin
"""
from math import sqrt

from sympy import floor

def SieveofEratos(n):
    
    A=[True]*(n-1)
    for i in range(2,floor(sqrt(n))):
        if A[i-2]==True:
            for j in range(i**2,n+1,i):
                A[j-2]=False
    outputArg1=[i if A[i] else [] for i in range(n-1)]
    
    return outputArg1

print(SieveofEratos(100000))