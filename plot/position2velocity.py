# -*- coding: utf-8 -*-
"""
Created on Mon Jul 19 00:20:45 2021

@author: rodin
"""

import matplotlib.pyplot as plt
import numpy as np

def get_input():
    
    data=[]
    with open('pos.dat','r') as f_ID:
        for line in f_ID:
            if len(line)<4:
                s=eval(line)
            else:
                tempvar=line.split()
                data.append([eval(tempvar[0]),eval(tempvar[1])])
        f_ID.close()
    
    return s, np.array(data)

def calc_velocity(x,y,s):
    
    vx=x[1:]-x[0:-1]
    vx*=(1/s)
    
    vy=y[1:]-y[0:-1]
    vy*=(1/s)
    
    return vx, vy
    
def plotfunc_v2(x,y,s):
    
    t=np.linspace(0,s*len(x)-1,len(x))
    
    plt.figure()
    plt.subplot(1,2,1)
    plt.plot(t,x,'k-')
    plt.xlabel('time (s)')
    plt.ylabel('Velocity x (m/s)')
    plt.title('Time vs Velocity curve')
    
    plt.subplot(1,2,2)
    plt.plot(t,y,'r--o')
    plt.xlabel('time (s)')
    plt.ylabel('Velocity y (m/s)')
    plt.title('Time vs Velocity curve')
    
    plt.show()
    

def plotfunc(x,y):
    
    plt.plot(x,y,'k-')
    plt.xlabel('x values')
    plt.ylabel('y values')
    plt.title('Position curve')
    plt.show()
    
s, data=get_input()
plotfunc(data[:,0],data[:,1])

vx, vy=calc_velocity(data[:,0],data[:,1],s)
plotfunc_v2(vx,vy,s)

    
    
