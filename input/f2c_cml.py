# -*- coding: utf-8 -*-
"""
Created on Thu Sep 30 02:25:54 2021

@author: rodin
"""

import sys

def get_input():
    
    F=eval(sys.argv[1])
    #F=eval(input('Please enter a value for F\n>> '))
    
    return F

def F2C(F):
    
    C=(F-32)*(5/9)
    
    print(C)
    
F=get_input()
F2C(F)