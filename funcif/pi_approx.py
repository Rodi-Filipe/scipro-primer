# -*- coding: utf-8 -*-
"""
Created on Sat Jun 26 21:07:43 2021

@author: rodin
"""

def func0(n):
    
    from math import cos, sin, pi
    
    x=[0.5*cos((2*pi*i)/n) for i in range(n+1)]
    
    y=[0.5*sin((2*pi*i)/n) for i in range(n+1)]
    
    return x, y

def pathlength(x,y):
    
    from math import sqrt
    L=0
    for i in range(1,len(x)):
        L+=sqrt((x[i]-x[i-1])**2+(y[i]-y[i-1])**2)
        
    return L

def printfunc(M):
    
    from math import pi
    
    print('   n             error')
    for i in range(2,M+1):
        n=2**i
        x, y=func0(n)
        L=pathlength(x,y)
        print('%8d  %15.10f' %(n,abs(pi-L)))
    
    
printfunc(25)
        
        