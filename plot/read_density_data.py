# -*- coding: utf-8 -*-
"""
Created on Sun Jul 18 01:45:53 2021

@author: rodin
"""

import sys

import numpy as np

import matplotlib.pyplot as plt 

def get_input():
    
    outputArg1=[]
    f_ID=open(sys.argv[1],'r')
    line=f_ID.readline()
    while line:
        tempvar=line.split()
        try: 
            if tempvar[0].count('#'):
                pass
            else:
                outputArg1.append([eval(tempvar[0]),eval(tempvar[1])])
        except:
            pass 
        line=f_ID.readline()          
    f_ID.close()
    
    return np.array(outputArg1)

def plotfunc(data):
    
    plt.plot(data[:,0],data[:,1],'g--o')
    plt.xlabel('temperature')
    plt.ylabel('density')
    plt.title('temperature vs density plot')
    plt.show()

data=get_input()
plotfunc(data)
    
    
    