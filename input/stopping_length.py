# -*- coding: utf-8 -*-
"""
Created on Wed Jul  7 01:54:34 2021

@author: rodin
"""

import sys

def get_input():
    
    v=eval(sys.argv[1])*(1e3/3600)
    frict_coef=eval(sys.argv[2])
    return v, frict_coef

def braking_cal(v,frict_coef):
    
    g=9.81
    d=(1/2)*(v**2/(frict_coef*g))
    
    return d
v, frict_coef=get_input()

print(braking_cal(v,frict_coef))