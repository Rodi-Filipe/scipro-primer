# -*- coding: utf-8 -*-
"""
Created on Sun Aug  1 01:15:30 2021

@author: rodin
"""

import os
import numpy as np
import matplotlib.pyplot as plt
from matplotlib import animation
from math import cos, sin, pi, sqrt

def draw_circle(r):
    
    for rvalues in np.linspace(0,r,10000):
        x=np.array([ rvalues*cos((2*pi*i) / n) for i in range(n+1) ])
        y=np.array([ rvalues*sin((2*pi*i) / n) for i in range(n+1) ])
        
        plt.plot(x,y,'m')
    
    ax=plt.gca()

    return ax

def xypoint(t):
    
    x=a*cos(omega * t)
    
    y=b*sin(omega * t)
    
    xvec.append(x)
    yvec.append(y)
    
    return x, y, xvec, yvec

def init():
    
    lines[1].set_data([],[])
    plt.axis([-a-1,a+1,-b-1,b+1])
    
    return lines
    
def frames(args):
    
    t, lines = args
    
    x1, y1, x2, y2 = xypoint(t)
    
    lines[0].set_data(x1,y1)
    lines[0].set_marker('o')
    lines[0].set_color('r')
    lines[0].set_markersize(10)
    lines[1].set_data(x2,y2)
    lines[1].set_color('r')
    ax.set_title('Veclocity = %-8.4f' % (omega * sqrt((a**2 * (sin(omega*t)) **2) + (b**2 * (cos(omega*t)) **2))))
    
    return lines


n = eval(input('Please enter an n value\n>>'))
a = eval(input('Please enter an a values\n>>'))
b = eval(input('Please enter a b values\n>>'))
omega = eval(input('Please enter an omega value\n>>'))
xvec=[]; yvec=[]

fig = plt.figure()
ax = draw_circle(b/2)
ax.set_axis_off()
lines = ax.plot([],[],[],[])
all_args=[ (0 +i*((2*pi/omega - 0)/n), lines) for i in range(n+1) ]

anim=animation.FuncAnimation(fig,frames,all_args,init_func=init,interval=150,blit=True)

anim.save('planet_orbit_movie.mp4',fps=5)

os.system('planet_orbit_movie.mp4')