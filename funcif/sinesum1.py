# -*- coding: utf-8 -*-
"""
Created on Sat Jun 26 23:08:22 2021

@author: rodin
"""

from math import pi, sin

def S(t, n, T=50):
    
    runsum=0
    for i in range(1,n+1):
        tempvar=(4/pi)*(1/(2*i-1))*sin((2*(2*i-1)*pi*t)/T)
        runsum+=tempvar
    
    return runsum

def f(t,T=50):
    
    if t>0 or t<(T/2):
        outputArg1=1
    elif t==T/2:
        outputArg1=0
    elif t>T/2 or t<T:
        outputArg1=-1
    
    return outputArg1

def printfunc(n,a):
    
    print('  n     a     t    error')
    for i in n:
        for j in a:
            tempvar= abs(f(j*pi*2,T=2*pi)-S(j*2*pi,i,T=2*pi))
            print('%4d %5.2f  %5.2f  %5.3f' \
                  %(i, j, j*2*pi, tempvar))
    
printfunc([1,3,5,10,30,100,500],[0.01,0.25,0.49])
        