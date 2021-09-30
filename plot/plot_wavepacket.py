# -*- coding: utf-8 -*-
"""
Created on Sun Jul 25 02:40:55 2021

@author: rodin
"""

import numpy as np
import matplotlib.pyplot as plt
import time
import glob, os 

for filename in glob.glob('tmp*.png'): 
    os.remove(filename)

def graph():
    
    t=1.5
    x=np.linspace(-4,4,1000)
    y=np.exp(-(x-3*t)**2)*np.sin(3*np.pi*(x-t))
    
    plt.plot(x,y)
    plt.xlabel('wave distance')
    plt.ylabel('wave length')
    plt.title('Wave packet')
    plt.show()
    
def animate(tvalues):
    
    plt.ion()

    x=np.linspace(-4,4,1000)
    y=np.exp(-(x-3*tvalues[0])**2)*np.sin(3*np.pi*(x-tvalues[0]))
    
    lines=plt.plot(x,y)
    plt.axis([min(x)-0.5,max(x)+0.5,-(max(y)+0.5), max(y)+0.5])
    plt.xlabel('wave distance')
    plt.ylabel('wave length')
    plt.title('Wave packet')
    
    counter=0
    for t in tvalues:
        x=np.linspace(-4,4,1000)
        y=np.exp(-(x-3*t)**2)*np.sin(3*np.pi*(x-t))
        lines[0].set_ydata(y)
        #plt.draw()
        plt.pause(1.5)
        plt.savefig('tmp_%04d.png' % counter)
        counter+=1
    #plt.show()
    #os.system('ffmpeg -i tmp_%04d.png -r 5 -vcodec flv wavepacket.flv')

animate(np.linspace(0,5,100))
