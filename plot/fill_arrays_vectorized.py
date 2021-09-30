# -*- coding: utf-8 -*-
"""
Created on Thu Jul 15 02:34:32 2021

@author: rodin
"""
import numpy as np

from math import sqrt, pi

def fillfunc(n):
    
    xlist=np.linspace(0,10,n)
    hlist=(1/(sqrt(2*pi)))*(np.exp(-0.5*xlist**2))    
    
    return xlist, hlist

xlist, hlist=fillfunc(10000000)

