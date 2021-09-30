# -*- coding: utf-8 -*-
"""
Created on Thu Sep 23 19:33:41 2021

@author: rodin
"""

import matplotlib.pyplot as plt
import numpy as np

class LagrangeInterpolation(object):
    
    def __init__(self,arg1,arg2,arg3=None):
        
        self.p1=arg1
        self.p2=arg2
        self.p3=arg3
        
    def __call__(self,x):
        
        if callable(self.p1) and isinstance(self.p2,list) and isinstance(self.p3,(float,int)):
            xp=np.linspace(self.p2[0],self.p2[1],self.p3)
            yp=self.p1(xp)
            return p_L(x,xp,yp)
        else:
            xp=self.x
            yp=self.y
        
        return p_L(x,xp,yp)
   
    def plot(self):
        
        if callable(self.p1) and isinstance(self.p2,list) and isinstance(self.p3,(float,int)):
            xp=np.linspace(self.p2[0],self.p2[1],self.p3)
            yp=self.p1(xp)
        else:
            xp=self.p1
            yp=self.p2
        
        xvec=np.linspace(xp.min(),xp.max(),1000)
        yvec=np.array([p_L(xvalue,xp,yp) for xvalue in xvec])
            
        plt.plot(xvec,yvec,'y--')
        plt.xlabel('x value')
        plt.ylabel('y values')
        plt.title('Exact curve & Langrange interpolation function curve')
        plt.plot(xp,yp,'bo')
        plt.legend(['Langrange interpolation curve','Discrete Points'])
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