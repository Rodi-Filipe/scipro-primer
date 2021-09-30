# -*- coding: utf-8 -*-
"""
Created on Sun Sep 26 19:42:11 2021

@author: rodin
"""

import numpy as np
from matplotlib.pyplot import plot

class Heaviside():
    
    def __init__(self,eps=None):
        
        self.eps=eps
    
    def __call__(self,value):
        
        if self.eps==None:
            outputArg1=np.where(value>0,1,0)
        else:
            outputArg1=np.where(value>self.eps,1.0,0.0)
            tempvar=0.5+value/(2*self.eps)+1/(2*np.pi)*np.sin((np.pi*value)/self.eps)
            outputArg1+=np.where(np.logical_and(value>=-self.eps,value<=self.eps),tempvar,0.0)
    
        return outputArg1

    def plot(self,xmin,xmax):
        
        x=np.linspace(xmin,xmax,100000)
        y=self.__call__(x)
        
        return x, y

H=Heaviside()
print(H(0.1))
H=Heaviside(eps=0.8)
print(H(0.1))

H=Heaviside()
x=np.linspace(-1,1,11)
print(H(x))
H=Heaviside(eps=0.8)
print(H(x))

H = Heaviside() 
x, y = H.plot(xmin=-4, xmax=4) # x in [-4, 4] 
plot(x, y)
 
H = Heaviside(eps=1) 
x, y = H.plot(xmin=-4, xmax=4)
plot(x,y)

 