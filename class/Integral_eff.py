# -*- coding: utf-8 -*-
"""
Created on Mon Sep 27 00:19:01 2021

@author: rodin
"""

import numpy as np

class Integral(object):
    
    def __init__(self,f,n):
        
        self.f=f
        self.n=n
        
    def __call__(self,x):
        
        g,n=self.f,self.n
        
        if isinstance(x,(int,float)):
            x=np.linspace(0,x,n+1)
            
        fvec=np.zeros_like(x)
        fvec[0]=0
        
        for k in range(n):
            nk=int(n*((x[k+1]-x[k])/(x[-1]-x[0])))
            nk = nk if nk !=0 else 1
            fvec[k+1]=trapzint(g,x[k],x[k+1],nk)
        return fvec
        
        '''if isinstance(x,(int,float)):
            x=np.linspace(0,x,n+1)

        fvec=np.zeros_like(x)
        fvec[0]=0
        
        for i in range(1,n+1):
            fvec[i]=fvec[i-1]+0.5*(x[i]-x[i-1])*(g(x[i-1])+g(x[i]))
        
        return fvec[-1]'''

def trapzint(f,a,b,n):
    
    h=(b-a)/n
    outputArg1=0
    
    for i in range(n):
        x_o=a+i*h
        x_1=a+(i+1)*h
        outputArg1+=(1/2)*h*(f(x_o)+f(x_1))
    
    return outputArg1

def test_Integral():
    
    x=50
    exact=5500
    
    f=Integral(lambda x: 4*x+10,99999)
    result=np.sum(f(x))
    
    assert abs(result-exact)<1E-6, 'Test failed! %s != to %s' %(result, exact)
    
test_Integral()