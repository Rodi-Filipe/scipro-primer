# -*- coding: utf-8 -*-
"""
Created on Fri Jul  2 18:23:25 2021

@author: rodin
"""

def get_input(NumHeaderLines=3):
    
    f_ID=open('Fdeg.dat','r')
    F=[]
    tempvar1=f_ID.readlines()
    
    for i in range(NumHeaderLines,len(tempvar1)):
        tempvar2=tempvar1[i].split(sep=' ')[2]
        F.append(eval(tempvar2))
    
    f_ID.close()
    return F

def F2C(F):
    
    C=[(i-32)*(5/9) for i in F]
    print(C)
    
F=get_input()
F2C(F)
