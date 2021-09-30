# -*- coding: utf-8 -*-
"""
Created on Sat Aug 14 01:21:50 2021

@author: rodin
"""
import sys
from numpy import *
import matplotlib.pyplot as plt
from scitools.StringFunction import StringFunction
import os

def get_input():
    
    if len(sys.argv[1:]) == 3:
        f=sys.argv[1]
        xmin=float(sys.argv[2])
        xmax=float(sys.argv[3])
    else:
        raise IndexError('Not enough input arguments!')
        sys.exit(1)
    
    return f, xmin, xmax
    
def graph(f,xmin,xmax):
    
    x=arange(xmin,xmax,(xmax-xmin)/1000)
    
    f=StringFunction(f)
    
    f.vectorize(globals())
    
    y=f(x)
    
    plt.plot(x,y,'c:')
    plt.xlabel('x values')
    plt.ylabel('y values')
    plt.title('My curve')
    plt.savefig('tmp.png')
    
    os.system('tmp.png')
    
f, xmin, xmax=get_input()
graph(f,xmin,xmax)
    