# -*- coding: utf-8 -*-
"""
Created on Tue Aug  3 23:31:32 2021

@author: rodin
"""
import numpy as np
import matplotlib.pyplot as plt
from matplotlib import animation
import os

def v(r,R,beta,mu,n):
    
    outputArg1=(beta/2*mu)**(1/n) * n/(n + 1) * (R**(1 + 1/n) - r**(1+1/n))
        
    return outputArg1

def get_input():
    
    R = float(input('Please enter a value for R\n>>'))
    beta = float(input('Please enter a value for beta\n>>'))
    mu = float(input('Please enter a value for mu\n>>'))
    n = float(input('Please enter a value for n\n>>'))
    
    return R, beta, mu, n

def graph(R,beta,mu,n):
    
    r=np.linspace(0,R,1000)
    v_var=v(r,R,beta,mu,n)
    plt.plot(r,v_var)
    plt.xlabel('radius')
    plt.ylabel('velocity')
    plt.title('Velocity profile for pipeflow')
    
    plt.show()

def init_params():
    
    fig, ax=plt.subplots()
    lines=ax.plot([],[])
    
    all_args=[(1 + i*(0.001-1)/50 ,lines) for i in range(50+1)]
    
    return fig, lines, ax, all_args

def init():
    
    ax.set_xlabel('radius')
    ax.set_ylabel('velocity')
    ax.set_title('Velocity profile for pipeflow')
    ax.set_xlim(0.05,1.05)
    ax.set_ylim(0.05,1.05)
                
    return lines

def frames(args):
    
    nvalue, lines = args
    r=np.linspace(0,R,1000)
    y=v(r,R,beta,mu,nvalue)
    y/=v(0,R,beta, mu, nvalue)
    
    lines[0].set_data(r,y)
    lines[0].set_color('c')
    lines[0].set_linestyle('--')
    
    ax.legend(['n=%-8.5f' % nvalue])
    
    return lines    
       
def animate(fig,all_args):
     
    anim=animation.FuncAnimation(fig,frames,all_args,init_func=init,interval=150,blit=True)

    anim.save('velocity_pipeflow_movie.mp4',fps=5)
    
    os.system('velocity_pipeflow_movie.mp4')
    
     
R, beta, mu, n=get_input()

graph(R,beta,mu,n)

fig, lines, ax, all_args = init_params()

animate(fig,all_args)