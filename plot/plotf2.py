# -*- coding: utf-8 -*-
"""
Created on Sat Aug 14 03:42:38 2021

@author: rodin
"""

import sys
from numpy import *
import matplotlib.pyplot as plt
from scitools.StringFunction import StringFunction
import os

def get_input():
    
    if len(sys.argv[1:]) == 3:
        try:
            f=StringFunction(str(sys.argv[1]))
            xmin=float(sys.argv[2])
            xmax=float(sys.argv[3])
            n=501
            
            if xmin > xmax:
                raise ValueError
                
        except:
            print('Invalid input!')
            sys.exit(1)
            
    elif len(sys.argv[1:]) == 4:
        try:
            f=StringFunction(str(sys.argv[1]))
            xmin=float(sys.argv[2])
            xmax=float(sys.argv[3])
            n=int(sys.argv[4])
            
            if xmin > xmax:
                raise ValueError('Invalid input!')
                sys.exit(1)
                
        except ValueError:
            print('Invalid input!')
            sys.exit(1)
            
    else:
        raise IndexError('Not enough input arguments!')
        sys.exit(1)
    
    return f, xmin, xmax, n
    
def graph(f,xmin,xmax, n):
    
    x=arange(xmin,xmax,(xmax-xmin)/n)
    
    f.vectorize(globals())
    
    y=f(x)
    
    plt.plot(x,y,'c:')
    plt.xlabel('x values')
    plt.ylabel('y values')
    plt.title('My curve')
    plt.savefig('tmp.png')
    
    os.system('tmp.png')
    
f, xmin, xmax, n = get_input()

graph(f, xmin, xmax, n)