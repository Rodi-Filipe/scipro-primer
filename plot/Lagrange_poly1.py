# -*- coding: utf-8 -*-
"""
Created on Sun Jul 25 00:48:34 2021

@author: rodin
"""

import numpy as np
import matplotlib.pyplot as plt

def L_k(x,k,xp,yp):
    
    tempvar=xp[xp!=xp[k]].copy()
    outputArg1=np.prod((x-tempvar)/(xp[k]-tempvar))
    
    return outputArg1

def p_L(x,xp,yp):
    
    runsum=0
    for i in range(len(yp)):
        runsum+=yp[i]*L_k(x,i,xp,yp)
        
    return runsum

def test_p_L(xp,yp):
    
    tempvar=[abs(yp[ind]-p_L(xvalue,xp,yp)) <1E-7 for ind, xvalue in enumerate(xp)]
    
    tempvar=np.array(tempvar,dtype=bool)
    
    assert tempvar.all(), 'Test failed!'
 
def graph(f,n,xmin,xmax,resolution=1001):
    
    xp=np.linspace(0,np.pi,n)
    yp=f(xp)
    
    xnew=np.linspace(xmin,xmax,resolution)
    ynew=np.array([p_L(xvalue,xp,yp) for xvalue in xnew])
    plt.plot(xnew,ynew,'ro')
    plt.xlabel('x value')
    plt.ylabel('y values')
    plt.title('Exact curve & Langrange interpolation function curve')
    plt.plot(xp,yp,'b--')
    plt.legend(['Langrange interpolation function curve','Exact curve'])
    plt.show()
    
    
xp=np.linspace(0,np.pi,5)
yp=np.sin(xp)

test_p_L(xp,yp)

print(p_L(xp[1]+(xp[1]-xp[2])/2,xp,yp))
print(np.sin(xp[1]+(xp[1]-xp[2])/2))

graph(np.sin,30,0,np.pi,resolution=30)

    
