# -*- coding: utf-8 -*-
"""
Created on Sat Jul 31 18:37:46 2021

@author: rodin
"""

from math import e, sqrt, log
import numpy as np
import matplotlib.pyplot as plt
from matplotlib import animation

def T(z,t):
    
    outputArg1=T0 + A1 * np.exp(-a1 * z) * np.sin(omega1 * t - a1 * z) + \
        A2 * np.exp(-a2 * z) * np.sin(omega2 * t - a2 * z)
    
    return outputArg1

def init():
    
    lines[0].set_data([],[])
    plt.axis([0, D, (T0 - A2 - A1), (T0 + A2 + A1)])
    plt.xlabel('Time (s)')
    plt.ylabel('Temperature (C)')
    plt.title('Temperature variations curve')
    
    return lines

def frames(args):
    
    x, t, lines = args
    y=T(x,t)
    lines[0].set_data(x,y)
    
    return lines
  
T0 = 10
A1 = 15
A2 = 7
k = 10 ** (-6)
P1 = 24 * 60 * 60 * 365.
P2 = 24 * 60 * 60.
omega1 = 2 * np.pi / P1
omega2 = 2 * np.pi /  P2
a1 = sqrt(omega1/(2*k))
a2 = sqrt(omega2/(2*k))
D = -(1/a1) * log(0.001)

fig=plt.figure()
lines=plt.plot([],[])
all_args=[(np.linspace(0,D,500), 0 + i * (P2 / 10), lines) for i in range(50)]

anim=animation.FuncAnimation(fig,frames,all_args,init_func=init,interval=150,blit=True)

anim.save('heatwave2.mp4',fps=6)
    