# -*- coding: utf-8 -*-
"""
Created on Sun Sep 26 20:39:35 2021

@author: rodin
"""

import numpy as np
from matplotlib.pyplot import plot

class Heaviside():
    
    def __init__(self,L,R,eps=None):
        
        self.L=L
        self.R=R
        self.eps=eps
        
    def __call__(self,value):
        
        if self.eps==None:
            outputArg1=np.where(value>=self.L,1.0,0.0)*np.where(value<=self.R,1.0,0.0)
        else:
            term1 = np.where(value>self.L+self.eps,1.0,0.0)
            
            tempvar = 0.5+(value-self.L)/(2*self.eps)+1/(2*np.pi)*np.sin((np.pi*(value-self.L))/self.eps)
            
            term1 += np.where(np.logical_and(value>=self.L-self.eps,value<=self.L+self.eps),tempvar,0.0)
            
            term2 = np.where(value<self.R-self.eps,1.0,0)
            
            tempvar = 0.5+(-value+self.R)/(2*self.eps)+1/(2*np.pi)*np.sin((np.pi*(-value+self.R))/self.eps)
            
            term2 += np.where(np.logical_and(value>=self.R-self.eps,value<=self.R+self.eps),tempvar,0.0)
            
            outputArg1 = term1*term2
        
        return outputArg1

    def plot(self,xmin,xmax):
        
        x=np.linspace(xmin,xmax,100000)
        y=self.__call__(x)
        
        return x, y
    
    
H=Heaviside(2,5)
print(H(0.1))
H=Heaviside(2,5,eps=0.8)
print(H(0.1))

H=Heaviside(5,20)
x=np.linspace(-1,1,11)
print(H(x))
H=Heaviside(5,20,eps=0.8)
print(H(x))

H = Heaviside(3,7) 
x, y = H.plot(xmin=0, xmax=9) # x in [-4, 4] 
plot(x, y)
 
H = Heaviside(3,7,eps=1) 
x, y = H.plot(xmin=0, xmax=9)
plot(x,y)

 