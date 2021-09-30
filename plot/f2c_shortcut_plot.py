# -*- coding: utf-8 -*-
"""
Created on Fri Jul 16 13:16:59 2021

@author: rodin
"""

import numpy as np
import matplotlib.pyplot as plt

def get_values(n):
    
    F=np.linspace(-20,120,n)
    C1=(F-30)/2
    C2=(F-32)*5/9
    
    return F, C1, C2

def plotfunc(F,C1,C2):
    
    plt.plot(F,C1,'r--',F,C2,'y-')
    plt.xlabel('F values')
    plt.ylabel('C values')
    plt.title('Celsius vs Fahrenheit plot')
    plt.legend(['approximation','exact'])
    plt.show()


F, C1, C2=get_values(20)

plotfunc(F,C1,C2)
