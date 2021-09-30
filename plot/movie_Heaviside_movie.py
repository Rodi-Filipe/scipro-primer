# -*- coding: utf-8 -*-
"""
Created on Sat Jul 31 17:39:46 2021

@author: rodin
"""

import os
from math import pi, sin
import numpy as np
import matplotlib.pyplot as plt
from matplotlib import animation

def H_eps(x, eps=0.01):
    
    if type(x)==np.ndarray:
        outputArg1=np.zeros_like(x)
        for i in range(len(x)):
            if x[i]<-eps:
                outputArg1[i]=0
            elif x[i]>=-eps and x[i]<=eps:
                outputArg1[i]=0.5+x[i]/(2*eps)+1/(2*pi)*sin((pi*x[i])/eps)
            elif x[i]>eps:
                outputArg1[i]=1
    else:
        if x<-eps:
            outputArg1=0
        elif x>=-eps and x<=eps:
            outputArg1=0.5+x/(2*eps)+1/(2*pi)*sin((pi*x)/eps)
        elif x>eps:
            outputArg1=1
                    
    return outputArg1


def init():
    
    lines[0].set_data([],[])
    plt.axis([-5,5,-1.5,1.5])
    plt.xlabel('x values')
    plt.ylabel('y values')
    plt.title('Smoothed Heavyside Curve')
    
    return lines


def frames(args):
    
    x, eps, lines = args
    y=H_eps(x,eps)
    lines[0].set_data(x,y)
    
    return lines
    
fig=plt.figure()
lines=plt.plot([],[])  
all_args=[(np.linspace(-5,5,100000), eps, lines) for eps in np.linspace(2,0,50)] 
anim=animation.FuncAnimation(fig,frames,all_args,init_func=init,interval=150,blit=True)

anim.save('movie_Heaviside.mp4',fps=6)

os.system('movie_Heaviside.mp4')