# -*- coding: utf-8 -*-
"""
Created on Tue Jul 27 23:12:49 2021

@author: rodin
"""

import numpy as np 
from math import cos, pi

x = np.linspace(0, 2, 20) 
y = x*(2 - x) 

import matplotlib.pyplot as plt 

plt.plot(x, y) 

ynew=np.cos(18*pi*x)

plt.plot(x,ynew)
plt.show()