# -*- coding: utf-8 -*-
"""
Created on Tue Jul 20 03:38:02 2021

@author: rodin
"""

import numpy as np
import sys

def polygon_area_vec(x,y):
    
    if isinstance(x,np.ndarray) and isinstance(y,np.ndarray):
        term1=np.dot(x[:-1],y[1:]) + x[-1]*y[0]
        
        term2=np.dot(y[:-1],x[1:]) + y[-1]*x[0]
        
        A=0.5*np.abs(term1-term2)
    else:
        raise ValueError('Invalid input!')
        sys.exit(1)
    
    return A

def  polygon_area(x,y):
    
    runsum1=0
    for i in range(len(x)):
        if i==len(x)-1:
            runsum1+=(x[i]*y[0])
        else:
            runsum1+=(x[i]*y[i+1])
    
    runsum2=0
    for i in range(len(y)):
        if i==len(x)-1:
            runsum2+=(y[i]*x[0])
        else:
            runsum2+=(y[i]*x[i+1])
            
    return 0.5*abs(runsum1-runsum2)


x=np.array([0,2,6,12,5,2])

y=np.array([0,9,10,20,8,2])

print(polygon_area(x,y))
print(polygon_area_vec(x,y))