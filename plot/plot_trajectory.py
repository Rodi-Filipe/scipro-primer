# -*- coding: utf-8 -*-
"""
Created on Fri Jul 16 13:35:04 2021

@author: rodin
"""

import argparse
import numpy as np
import matplotlib.pyplot as plt

def get_input():
    
    parser=argparse.ArgumentParser()
    
    parser.add_argument('--yo',type=float,default=0.,help='initial y value',metavar='yo')
    parser.add_argument('--theta',type=float,default=0.,help='theta value',metavar='theta')
    parser.add_argument('--vo',type=float,default=0.,help='initial velocity value',metavar='vo')
    parser.add_argument('--n',type=int,default=0,help='n value',metavar='n')
    
    args=parser.parse_args()
    
    return args.yo, args.theta, args.vo, args.n


def plotfunc(yo,theta,vo,n):
    
    g=9.81
    x=np.linspace(0,227.828,n)
    
    y=x*np.tan(theta)-1/(2*vo**2)*((g*x**2)/(np.cos(theta)**2))+yo

    plt.plot(x,y,'b--')
    plt.xlabel('x  values')
    plt.ylabel('y values')
    plt.title('Trajectory of a ball')
    plt.show()

yo,theta,vo,n=get_input()

plotfunc(yo,theta,vo,n)
    
    
    