# -*- coding: utf-8 -*-
"""
Created on Wed Jul 28 17:25:26 2021

@author: rodin
"""

import numpy as np
import matplotlib.pyplot as plt

def get_input():
    
    n=eval(input('Please enter the number of degree points\n>>'))
    T=np.linspace(0,100,n)
    
    return T

def calc_mu(T):
    
    T+=273.15
    A=2.414*10**-5
    B=247.8
    C=140
    
    outputArg1=A*10**(B/(T-C))
    
    return outputArg1

def graph(T,mu):
    
    plt.plot(T,mu,'r--o')
    plt.xlabel('temperature (C)')
    plt.ylabel('viscocity (Pa s)')
    plt.title('Viscocity of water curve')
    plt.show()

T=get_input()

mu=calc_mu(T)

graph(T, mu)