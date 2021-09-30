# -*- coding: utf-8 -*-
"""
Created on Sat Jul 31 01:13:44 2021

@author: rodin
"""

import numpy as np
import matplotlib.pyplot as plt

def graph():
    
    n=eval(input('Please enter the number of the length of the waves\n>> '))
    lambda_1=np.linspace(0.001,0.1,n)
    lambda_2=np.linspace(1,2,n)
    
    g=9.81
    s=7.9*10**-2
    rho=1000
    h=50
    tempvar1=((g*lambda_1)/(2*np.pi))*(1+s*(4*np.pi**2)/(rho*g*lambda_1**2))*np.tanh(2*np.pi*h/lambda_1)
    tempvar2=((g*lambda_2)/(2*np.pi))*(1+s*(4*np.pi**2)/(rho*g*lambda_2**2))*np.tanh(2*np.pi*h/lambda_2)
    c1=np.sqrt(tempvar1)
    c2=np.sqrt(tempvar2)
    
    plt.subplot(1,2,1)
    plt.plot(lambda_1,c1,'m--*')
    plt.xlabel('wave length')
    plt.ylabel('wave speed')
    
    
    plt.subplot(1,2,2)
    plt.plot(lambda_2,c2, 'r-o')
    plt.xlabel('wave length')
    plt.ylabel('wave speed')
    
    plt.show()

graph()