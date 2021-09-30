# -*- coding: utf-8 -*-
"""
Created on Fri Jul  2 18:09:05 2021

@author: rodin
"""

def get_input():
    
    f_ID=open('file1.txt','r')
    tempvar=f_ID.readlines()
    tempvar=tempvar[3].split(sep=' ')
    F=eval(tempvar[2])
    f_ID.close()
    
    return F

def F2C(F):
    
    C=(F-32)*(5/9)
    print(C)
    
F=get_input()
F2C(F)