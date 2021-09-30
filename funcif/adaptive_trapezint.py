# -*- coding: utf-8 -*-
"""
Created on Sat Jun 26 16:51:13 2021

@author: rodin
"""

def adaptive_trapezint(f,a,b,eps=1E-5):
        
    from math import sqrt
    
    h=1e-3
    counter=0
    x=a
    tempvar=[]
    while x<=b:
        tempvar2=abs((f(x+h)-2*f(x)+f(x-h))/h**2)
        tempvar.append(tempvar2)
        x+=h
        counter+=1
    
    tempvar=max(tempvar)
    
    h=sqrt(12*eps)*((b-a)*tempvar)**-0.5
        
    n=round((b-a)/h)
        
    """n=100000
    h=(b-a)/n
    tempvar=[0]*(n+1)
    for i in range(n+1):
        x=a+i*h
        tempvar[i]=abs((f(x+h)-2*f(x)+f(x-h))/h**2)
            
    tempvar=max(tempvar)
    h=sqrt(12*eps)*((b-a)*tempvar)**-0.5
        
    n=round((b-a)/h)"""
    
    outputArg1=(1/2)*h*(f(a)+f(b))
    
    for j in range(1,n):
        x=a+j*h
        outputArg1+=h*(f(x))
        
    return outputArg1, n
    

def printfunc(f):
    
    for f in f:
        result, n=adaptive_trapezint(f,b=pi,eps=1e-14,a=0)
        print('result=%5.2f for adaptive n=%d of function %s' %(result,n, f.__name__,))
    
    
        
from math import sin, cos, sinh, cosh, pi

f=[sin,cos,sinh,cosh,lambda x: 4*x**2+sin(x)]

printfunc(f)

    
            
        