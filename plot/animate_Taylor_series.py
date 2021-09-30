# -*- coding: utf-8 -*-
"""
Created on Tue Aug  3 19:08:45 2021

@author: rodin
"""

from math import factorial, pi
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.animation as animation
import os

def animate(fk, M, N, xmin, xmax, ymin, ymax, n, exact):
    
    def S(x,M,N):
        
        if type(x) == np.ndarray:
            tempvar=np.zeros((N+1,len(x)))
            for nvalues in range(M,N+1):
                tempvar[nvalues,:] = fk(x,nvalues)
            sum_var=np.sum(tempvar,axis=0)
        else:
            tempvar = [ fk(x,kvalues) for kvalues in range(M,N) ]
            sum_var = np.sum(tempvar) 
        
        return sum_var
            
    def init():
    
        lines[1].set_data([],[])
        plt.xlabel('x values')
        plt.ylabel('y values')
        
        plt.axis([xmin,xmax,ymin,ymax])
        plt.title('Taylor polynomials approx')
        
        return lines

    def frames(args):
    
        x, nvalues, lines = args
        
        y = S(x,M,nvalues)
    
        lines[1].set_data(x,y)
        lines[1].set_color('r')
        
        return lines
    
    fig = plt.figure()
    x=np.linspace(xmin,xmax,n)
    lines = plt.plot(x,exact(x),'c--',[],[])
    all_args=[ (x, i, lines) for i in range(M,N+1) ]
    
    anim=animation.FuncAnimation(fig,frames,all_args,init_func=init,interval=150,blit=True)

    anim.save('animate_Taylor_series_movie.mp4',fps=5)

    os.system('animate_Taylor_series_movie.mp4')

fk=lambda x, k: ((-x)**k) / factorial(k)
xmin=0
xmax=15
ymin=-0.5
ymax=1.4
M=0
N=30
n=1000
exact=lambda x: np.exp(-x)

animate(fk,M,N,xmin,xmax,ymin,ymax,n,exact)
        
    
    