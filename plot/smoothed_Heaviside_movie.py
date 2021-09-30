# -*- coding: utf-8 -*-
"""
Created on Thu Sep 30 16:11:49 2021

@author: rodin
"""

from math import sin, pi
import matplotlib.pyplot as plt
from matplotlib import animation
import numpy as np

import glob, os
# Remove old plot files
for filename in glob.glob('tmp_*.png'): os.remove(filename)


def init():
    
    lines[0].set_data([],[])
    plt.xlabel('x values')
    plt.ylabel('y values')
    plt.title('Smoothed Heaviside function')
    plt.axis([-6,6,-1.5,1.5])
    
    return lines

def H_eps(x, eps=0.01):
    
    outputArg1=np.zeros_like(x)
    outputArg1[x>eps]=1
    tempvar=x[np.logical_and(x>=-eps,x<=eps)]
    outputArg1[np.logical_and(x>=-eps,x<=eps)]=0.5+tempvar/(2*eps)+1/(2*pi)*np.sin((pi*tempvar)/eps)
    
    return outputArg1

def frames(args):
    
    x, eps, lines = args
    y=H_eps(x,eps)
    
    lines[0].set_data(x,y)
    
    return lines

fig=plt.figure()
lines=plt.plot([],[])
all_args=[(np.linspace(-6,6,1000),2-i*2/(1000-1), lines) for i in range(1000)]

anim=animation.FuncAnimation(fig,frames,all_args,init_func=init,interval=150,blit=True)

anim.save('smoothed_Heaviside_movie.mp4',fps=6)