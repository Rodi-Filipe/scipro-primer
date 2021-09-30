# -*- coding: utf-8 -*-
"""
Created on Sat Jul  3 01:58:21 2021

@author: rodin
"""

def ask_input():
    
    var1=eval(input('Please enter an input\n>> '))
    
    var2=type(var1)
    
    print(var1,var2)

ask_input()