# -*- coding: utf-8 -*-
"""
Created on Fri Jul  2 18:47:04 2021

@author: rodin
"""

import sys

def get_input():
    
    try:
        F=eval(sys.argv[1])
    except IndexError as e:
        raise IndexError('No comand line input given!')
        sys.exit(1)

    return F

def F2C(F):
    
    C=(F-32)*(5/9)
    
    print(C)
    
F=get_input()
F2C(F)