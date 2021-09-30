# -*- coding: utf-8 -*-
"""
Created on Sat Jul 31 16:41:45 2021

@author: rodin
"""

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
    plt.title('wave packet function')
    plt.axis([-6,6,-1.5,1.5])
    
    return lines

def frames(args):
    
    x, t, lines = args
    y=np.exp(-1*(x-3*t)**2)*np.sin(3*np.pi*(x-t))
    
    lines[0].set_data(x,y)
    
    return lines

fig=plt.figure()
lines=plt.plot([],[])
all_args=[(np.linspace(-6,6,10000),i, lines) for i in np.linspace(-1,1,100)]

anim=animation.FuncAnimation(fig,frames,all_args,init_func=init,interval=150,blit=True)

anim.save('plot_wavepacket_movie.gif',fps=6)
