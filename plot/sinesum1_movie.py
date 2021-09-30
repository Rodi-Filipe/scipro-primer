# -*- coding: utf-8 -*-
"""
Created on Wed Aug 11 03:51:39 2021

@author: rodin
"""
import numpy as np
import os
from math import pi
import matplotlib.pyplot as plt
import matplotlib.animation as animation



def S(t, n, T=2*pi):
    
    if type(t)==np.ndarray or type(t)==list:
        runsum=np.zeros(len(t))
        for i in range(1,n+1):
            tempvar=(4/np.pi) * (1/(2*i-1)) * np.sin((2*(2*i-1)*np.pi*t)/T)
            runsum+=tempvar 
    else:
        runsum=0
        for i in range(1,n+1):
            tempvar=(4/np.pi) * (1 / (2*i-1) ) * np.sin( (2*(2*i-1)*np.pi*t) / T )
            runsum+=tempvar
    return runsum

def init_params():
    
    fig, ax=plt.subplots()
    lines=ax.plot([],[])
    
    all_args=[(i, lines) for i in range(1000)]
    
    return fig, lines, ax, all_args

def init():
    
    ax.set_xlabel('x values')
    ax.set_ylabel('y values')
    ax.set_title('Sum of Sines Approximation Curves')
    ax.set_xlim(0,20*pi)
    ax.set_ylim(-2,2)
                
    return lines

def frames(args):
    
    nvalue, lines = args
    t=np.arange(0,20*pi,pi/4)
    y=S(t,nvalue)
    
    lines[0].set_data(t,y)
    lines[0].set_color('c')
    lines[0].set_linestyle('--')
    
    ax.legend(['n=%-8.5f' % nvalue])
    
    return lines    
       
def animate(fig,all_args):
     
    anim=animation.FuncAnimation(fig,frames,all_args,init_func=init,interval=150,blit=True)

    anim.save('sinesum1_movie.mp4',fps=5)
    
    os.system('sinesum1_movie.mp4')
    
fig, lines, ax, all_args = init_params()
animate(fig,all_args)