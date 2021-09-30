# -*- coding: utf-8 -*-
"""
Created on Thu Jul 15 02:27:15 2021

@author: rodin
"""

from math import sqrt, exp, pi

import numpy as np

def fillfunc(n):
    
    xlist=np.zeros(n,dtype=float)
    hlist=np.zeros(n,dtype=float)
    
    for i in range(len(xlist)):
        xlist[i]=i
        hlist[i]=1/(sqrt(2*pi))*exp(-0.5*i**2)
    
    return xlist, hlist

xlist1, hlist1=fillfunc(20)