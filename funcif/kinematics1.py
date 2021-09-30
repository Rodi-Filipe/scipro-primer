# -*- coding: utf-8 -*-
"""
Created on Mon Jun 28 01:46:58 2021

@author: rodin
"""

from math import exp, cos, sinh, sqrt

def func0(n):
    
    a=eval(input('Enter an a value\n>> '))
    b=eval(input('Enter a b value\n>> '))
    outputArg1=[a+i*((b-a)/(n-1)) for i in range(n)]
    outputArg2=[i**3+i**2 for i in outputArg1]
    
    return outputArg1, outputArg2

def kinematics(t,x):
    
    outputArg1=[0]*len(x)
    outputArg2=[0]*len(x)
    for i in range(1,len(x)-1):
        outputArg1[i]=(x[i+1]-x[i-1])/(t[i+1]-t[i-1])
        outputArg2[i]=2*((t[i+1]-t[i-1])**-1)*\
            ((x[i+1]-x[i])/(t[i+1]-t[i])-(x[i]-x[i-1])/(t[i]-t[i-1]))
            
    return outputArg1, outputArg2

def printfunc(t,x,v,accel):
    
    print('      t         x         v       accel')
    print('-----------------------------------------')
    for i in range(len(t)):
        print('%9.2f %9.2g %9.3g %9.3g' %(t[i], x[i],\
                v[i], accel[i]))

    
t, x=func0(100)

v, accel=kinematics(t,x)

printfunc(t,x,v,accel)

    
    