# -*- coding: utf-8 -*-
"""
Created on Thu Sep 23 18:39:16 2021

@author: rodin
"""
import matplotlib.pyplot as plt
import numpy as np

class LagrangeInterpolation(object):
    
    def __init__(self,x,y):
        
        self.x=x
        self.y=y
        
    def __call__(self,x):
        
        return p_L(x,self.x,self.y)
    
    def plot(self):
        
        xvec=np.linspace(min(self.x),max(self.x),10000)
        yvec=np.array([p_L(xvalue,self.x,self.y) for xvalue in xvec])
        
        plt.plot(xvec,yvec,'y--')
        plt.xlabel('x value')
        plt.ylabel('y values')
        plt.title('Exact curve & Langrange interpolation function curve')
        plt.plot(self.x,self.y,'b-o')
        plt.legend(['Langrange interpolation function curve','Discrete Points'])
        plt.show()

def L_k(x,k,xp,yp):
    
    tempvar=xp[xp!=xp[k]].copy()
    outputArg1=np.prod((x-tempvar)/(xp[k]-tempvar))
    
    return outputArg1

def p_L(x,xp,yp):
    
    runsum=0
    for i in range(len(yp)):
        runsum+=yp[i]*L_k(x,i,xp,yp)
        
    return runsum        