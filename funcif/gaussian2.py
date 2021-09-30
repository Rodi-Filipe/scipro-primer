# -*- coding: utf-8 -*-
"""
Created on Sun Jun 27 00:25:49 2021

@author: rodin
"""

from math import sqrt, pi, exp

def gauss(x, m=0, s=1):
    
    tempvar1=1/(sqrt(2*pi)*s)
    
    tempvar2=exp(-0.5*((x-m)/s)**2)
    
    return tempvar1*tempvar2

def printfunc(m,s,n):
    
    
    a=m-5*s
    b=m+5*s
    h=(b-a)/(n-1)
    
    print('\n  x          f(x)')
    print('-----------------------')
    for i in range(0,n):
        x=a+i*h
        tempvar1=gauss(x,m,s)
        print('%6.2f  %13.9f' %(x, tempvar1))
        

printfunc(2,5,100)