# -*- coding: utf-8 -*-
"""
Created on Sat Jul 10 19:51:47 2021

@author: rodin
"""

from math import factorial

def binomial(x,n,p):
    
    outputArg1=(factorial(n)/(factorial(x)*factorial(n-x)))*p**x*(1-p)**(n-x)
    
    return outputArg1

print(binomial(2,5,0.5)*100)

print(binomial(4,4,1/6)*100)

print((1-binomial(0, 5, 1/120))*100)

runsum=0

for i in range(1,6):
    runsum+=binomial(i,5,1/120)

print(runsum*100)