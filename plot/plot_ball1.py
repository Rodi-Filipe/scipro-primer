# -*- coding: utf-8 -*-
"""
Created on Thu Sep 30 15:01:21 2021

@author: rodin
"""


import matplotlib.pyplot as plt
import numpy as np

vo=10
g=9.81

t=np.r_[0:2*vo/g:100j]
y=vo*t-0.5*g*t**2
plt.plot(t,y,'k:')
plt.xlabel('time (s)')
plt.ylabel('height (m)')
plt.title('position vs time curve')
plt.show()