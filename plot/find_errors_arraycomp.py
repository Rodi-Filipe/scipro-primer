# -*- coding: utf-8 -*-
"""
Created on Sat Aug 21 02:50:18 2021

@author: rodin
"""

import numpy as np

def prog1():
    
    x=np.linspace(0,1,3)
    y=np.zeros(len(x))

    for i in range(len(x)):
        y[i]=x[i]+4
        print(x[i],y[i])
    
    print()
    for xi, yi in zip(x,y):
        yi=xi+5
        print(xi,yi)
        
prog1()