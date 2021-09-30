# -*- coding: utf-8 -*-
"""
Created on Tue Jul  6 14:28:34 2021

@author: rodin
"""

import sys

def get_input():
    t=eval(sys.argv[1])
    vo=eval(sys.argv[2])
    
    return t, vo

def printy(t,vo):
    
    g=9.81
    print(vo*t -0.5*g*t**2)
    

t,vo=get_input()

printy(t,vo)