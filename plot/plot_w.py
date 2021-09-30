# -*- coding: utf-8 -*-
"""
Created on Mon Aug 16 00:33:52 2021

@author: rodin
"""

import numpy as np
import matplotlib.pyplot as plt

def graph():
    
    x=np.array([0,1,2,3,4])
    y=np.array([1,0,1,0,1])
    
    plt.plot(x,y,'k:')
    plt.xlabel('x values')
    plt.ylabel('y values')
    plt.title('W curve')
    
    plt.show()

graph()
    