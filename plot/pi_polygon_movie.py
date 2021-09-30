# -*- coding: utf-8 -*-
"""
Created on Sun Aug  1 00:40:16 2021

@author: rodin
"""
import os
import numpy as np
import matplotlib.pyplot as plt
from matplotlib import animation
from math import cos, sin, pi, sqrt

def get_input(n):
    
    x=np.array([0.5*cos((2*pi*i)/n) for i in range(n+1)])
    
    y=np.array([0.5*sin((2*pi*i)/n) for i in range(n+1)])
    
    return x, y

def pathlength(x,y):
    
    L=0
    for i in range(1,len(x)):
        L+=sqrt((x[i]-x[i-1])**2+(y[i]-y[i-1])**2)
        
    return L

def init():
    
    lines[0].set_data([],[])
    plt.axis([-1,1,-1,1])
    ax=plt.gca()
    ax.set_axis_off()
    
    return lines
    
def frames(args):
    
    n, lines = args
    
    x, y=get_input(n)
    ax=plt.gca()
    ax.set_title('Approximation error = %8.4f' % abs(np.pi-pathlength(x, y)))
    
    lines[0].set_data(x,y)
    lines[0].set_color('r')
    lines[0].set_marker('o')
    
    return lines

x,y=get_input(1000000)
fig = plt.figure()
lines = plt.plot([],[],x,y,'g-')
all_args=[(i, lines) for i in range(2,50)]

anim=animation.FuncAnimation(fig,frames,all_args,init_func=init,interval=0.3,blit=True)

anim.save('pi_polygon_movie.mp4',fps=5)

os.system('pi_polygon_movie.mp4')