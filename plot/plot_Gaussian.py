# -*- coding: utf-8 -*-
"""
Created on Thu Jul 15 02:59:51 2021

@author: rodin
"""

import numpy as np

from math import sqrt, pi

import matplotlib.pyplot as plt

def plotfunc(n):
    
    xlist=np.linspace(0,10,n)
    hlist=(1/(sqrt(2*pi)))*(np.exp(-0.5*xlist**2))
    
    plt.plot(xlist,hlist,'m-')
    plt.axis([min(xlist),max(xlist),min(hlist),max(hlist)])
    plt.xlabel('x values')
    plt.ylabel('y values')
    plt.title('Gaussian Function')
    plt.show()

plotfunc(500)