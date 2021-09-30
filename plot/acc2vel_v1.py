# -*- coding: utf-8 -*-
"""
Created on Sun Jul 18 20:30:13 2021

@author: rodin
"""

import sys
import numpy as np
import matplotlib.pyplot as plt
import argparse

def get_input():
    
    parser=argparse.ArgumentParser()
    
    parser.add_argument('--deltat',type=float,default=0.,help='time interval',metavar='delta_t')
    parser.add_argument('--k',type=int,default=0,help='iterable value',metavar='l')
    
    args=parser.parse_args()
    
    
    outputArg1=np.loadtxt('acc.dat',dtype=float)
    outputArg2=np.linspace(0,args.deltat*(len(outputArg1)-1),len(outputArg1))
    
    if args.k>len(outputArg1):
        raise ValueError('Invalid k value!')
        sys.exit(1)
    
    return outputArg1,outputArg2, args.deltat, args.k

def plotfunc(x,y):
    
    plt.plot(x,y,'r-')
    plt.xlabel('time')
    plt.ylabel('acceleration')
    plt.title('time vs acceleration')
    plt.show()
    
def calc_velocity(data,k,delta_t):
    
    runsum=0.5*data[0]+0.5*data[k]+sum(data[1:k])
    runsum=delta_t*runsum
    
    return runsum

def alt_calc_velocity(data,k,delta_t):
    
    outputArg1=delta_t*(0.5*data[0]+0.5*data[k])
    for i in range(1,k):
        outputArg1+=delta_t*data[i]
        
    return outputArg1

acc, t, delta_t, k=get_input()
plotfunc(t,acc)
print(calc_velocity(acc,k,delta_t))
print(alt_calc_velocity(acc,k,delta_t))
