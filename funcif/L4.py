# -*- coding: utf-8 -*-
"""
Created on Wed Jun 30 19:50:53 2021

@author: rodin
"""

def L4(x,epsilon=None,n=None,return_n=True):
    if epsilon != None and n == None:
        x = float(x)
        i = 1
        term = (1.0/i)*(x/(1+x))**i
        s = term
        while abs(term) > epsilon:
            i += 1
            term = (1.0/i)*(x/(1+x))**i
            s += term
        
        if return_n:
            return s
        else:
            return s, i
    elif n != None and epsilon == None:
         s = 0
         for i in range(1, n+1):
             s += (1.0/i)*(x/(1.0+x))**i
         
         if return_n:
            return s
         else:
            return s, i
    else:
         print('\nincompatible values,\neither both n and epsilon\nnot given or both values given')
         
L4(10,epsilon=1E-7,n=300,return_n=True)