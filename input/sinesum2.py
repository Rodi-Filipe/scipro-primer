# -*- coding: utf-8 -*-
"""
Created on Wed Jul  7 21:15:53 2021

@author: rodin
"""

import sys

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

def table(n,a,T):
    
    print('    n        a         t       error')
    for i in n:
        for j in a:
            tempvar= abs(f(j*T,T=T)-S(j*T,i,T=T))
            print('%7d %8.2f  %8.2f  %8.3f' \
                  %(i, j, j*2*pi, tempvar))

if __name__ == '__main__':
    if len(sys.argv)==4:
        n=eval(sys.argv[1])
        a=eval(sys.argv[2])
        T=eval(sys.argv[3])
        table(n,a,T)
    else:
        print('Invalid number of input arguments\n or not enought input arguments given') 

__all__ = ['S','f','table']