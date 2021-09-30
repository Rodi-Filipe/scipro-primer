# -*- coding: utf-8 -*-
"""
Created on Wed Jun 30 16:29:13 2021

@author: rodin
"""

from math import pi, cos 

def cos_sum(x,n=1000):
    c = 1
    outputArg1 = 0
    for i in range(n+1):
        outputArg1 += c
        c *= -((x**2)/(2*(i+1)*(2*(i+1)-1)))
    
    return outputArg1

def errorprint(k,n):
    
    #x=[(4+2*i)*pi for i in range(k)]
    #n=[5,25,50,100,200]
    
    for i in range(k+1):
        for j in range(len(n)+1):
            if i==0 and j==0:
                print('%6s' %('x'),end=' ')
            elif i==0 and j>0:
                print('%11d' % n[j-1],end=' ')
            elif j==0 and i>0:
                x = (4+2*(i-1))*pi
                print('%10.4f' % x,end=' ')
            else:
                print('%11.3g' % abs(cos(x)-cos_sum(x,n=n[j-1])),end=' ')
        print()


errorprint(10,[5,25,50,100,200])