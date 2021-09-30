# -*- coding: utf-8 -*-
"""
Created on Thu Jul 15 01:56:21 2021

@author: rodin
"""

from math import sqrt, exp, pi

def fillfunc(n):
    
    xlist=[i for i in range(n)]
    
    hlist=[1/(sqrt(2*pi))*exp(-0.5*i**2) for i in xlist]
    
    return xlist, hlist

xlist, hlist=fillfunc(200000)