# -*- coding: utf-8 -*-
"""
Created on Fri Aug 20 01:45:59 2021

@author: rodin
"""

import numpy as np
from math import exp
import matplotlib.pyplot as plt
import pprint

def v(x, mu=1E-6, exp=exp):
    
    try:
        numer=1-exp(x/mu)
        
        denom=1-exp(1/mu)
        
    except TypeError:
        
        numer = np.array([ 1-exp(x[k]/mu) for k in range(len(x)) ])
        
        denom = 1-exp(1/mu)
        
    return numer, denom, numer/denom

def prog1():
    
    x=np.linspace(0,1,100)

    f_list=[np.exp,exp]
    for xvalues in range(len(x)):
        for f in f_list:
            pprint.pprint(v(xvalues,1,exp=f))
    
def prog2():
    
    mu_list=[1,0.01,0.001]
    
    x=np.linspace(0,1,10000)
    for mu in mu_list:
        v_tuple = v(x,mu)
        
        plt.plot(x,v_tuple[-1],'c:')
        plt.xlabel('x values')
        plt.ylabel('y values')
        plt.title('V curve')
        plt.show()
        
def prog3():
    
    mu_list=[1,0.01,0.001]
    
    x=np.linspace(0,1,10000,dtype=np.longdouble)
    np.float
    for mu in mu_list:
        mu=np.longdouble(mu)
        pprint.pprint(v(x,mu))
        
def prog4():
    
    mu_list=[1,0.01,0.001]
    
    x=np.linspace(0,1,10000,dtype=np.float32)
    np.float
    for mu in mu_list:
        mu=np.float32(mu)
        pprint.pprint(v(x,mu))
        
prog1()

#prog2()

prog3()

prog4()