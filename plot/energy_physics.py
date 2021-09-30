# -*- coding: utf-8 -*-
"""
Created on Sun Aug 15 01:17:43 2021

@author: rodin
"""
import argparse
import numpy as np
import matplotlib.pyplot as plt

def get_input():

    parser=argparse.ArgumentParser() 
    
    parser.add_argument('--v0', default=0.0, help='Velocity Value',type=float,metavar='v0')
    parser.add_argument('--m', default=0.0, help='Mass Value',type=float,metavar='m')
    
    args=parser.parse_args()
    
    return args.v0, args.m

def f(v0=0):
    
    g=9.81
    t=np.linspace(0,2*v0/g,100)
    
    return v0*t-0.5*g*t**2

def poten(y,m=0):
    
    g=9.81

    return m*g*y

def kinetic(y,m=0):
    
    g=9.81
    yd=np.gradient(y,((2*v0/g)-0)/99)
    
    return 0.5*m*yd**2

def graph(m,v0):
    
    y=f(v0)
    p=poten(y,m)
    k=kinetic(y,m)
    plt.plot(y,'c_')
    plt.xlabel('x values')
    plt.ylabel('y values')
    plt.title('Energy concepts from physics')
    plt.plot(p,'b:')
    plt.plot(k,'g--')
    plt.plot(p+k,'r-')
    plt.legend(['Altitude curve','potential energy curve','kinetic energy curve','P+K curve'])
    plt.show()

v0, m = get_input()
graph(m,v0)
    
    
    
    
    


    
    