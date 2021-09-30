# -*- coding: utf-8 -*-
"""
Created on Tue Jul  6 14:24:10 2021

@author: rodin
"""

def get_input():
    t=eval(input('Please enter a value for t\n>> '))
    vo=eval(input('Please enter a value for v0\n>> '))
    
    return t, vo

def printy(t,vo):
    
    g=9.81
    print(vo*t -0.5*g*t**2)
    

t,vo=get_input()

printy(t,vo)
