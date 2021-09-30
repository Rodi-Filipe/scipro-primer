# -*- coding: utf-8 -*-
"""
Created on Thu Sep 30 18:47:42 2021

@author: rodin
"""

class Y: 
    
    def __init__(self, v0): 
        self.v0 = v0 
        self.g = 9.81 
    
    def __call__(self, t): 
        return self.v0*t - 0.5*self.g*t**2

class Derivative(object): 
    
    def __init__(self, f, h=1E-5): 
        self.f = f 
        self.h = float(h) 
    
    def __call__(self, x): 
        f, h = self.f, self.h # make short forms 
        return (f(x+h) - f(x))/h

from Y import Y

from Derivative import Derivative

y1=Y(5)

D1=Derivative(y1)

print(D1(0))
-25.819072981647647

print(5-9.81*(0))
-25.819023931715872

print(D1(0.5*5/9.81))
2.4999509500078787

print(5-9.81*(0.5*5/9.81))
2.5

print(D1(5/9.81))
-4.905000849930729e-05

print(5-9.81*(5/9.81))
0.0