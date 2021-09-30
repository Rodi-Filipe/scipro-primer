# -*- coding: utf-8 -*-
"""
Created on Sun Sep 26 21:36:23 2021

@author: rodin
"""

import numpy as np
from matplotlib.pyplot import plot

class PiecewiseConstant(object):
    
    def __init__(self,points,xmax):
        
        self.points = points
        self.xmax = xmax
        
    def __call__(self,x):
        
        outputArg1=np.zeros_like(x)
        outputArg1[x>=self.points[len(self.points)-1][1]]=self.points[-1][0]
        for i in range(len(self.points)-1):
            outputArg1[np.logical_and(x>=self.points[i][1],x<self.points[i+1][1])]=self.points[i][0]
    
        return outputArg1
    
    def plot(self):
        
        x=np.linspace(0,self.xmax,100)
        y=self.__call__(x)
        
        return x, y

f = PiecewiseConstant([(0.4, 1), (0.2, 1.5), (0.1, 3)], xmax=4) 
print(f(1.5), f(1.75), f(4)) 
x = np.linspace(0, 4, 21) 
print(f(x))

x, y=f.plot()
plot(x, y)
