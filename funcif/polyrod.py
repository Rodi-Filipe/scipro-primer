# -*- coding: utf-8 -*-
"""
Created on Sat Jun 26 02:02:00 2021

@author: rodin
"""

def poly(x,roots):
    
    runprod=1
    
    for i in roots:
        runprod *= (x-i)
    
    return runprod

print(poly(3.4,[5,3,20]))