# -*- coding: utf-8 -*-
"""
Created on Wed Aug 25 02:34:02 2021

@author: rodin
"""

import os
import numpy as np
import matplotlib.gridspec as gridspec
import matplotlib.pyplot as plt


def generate_dat():
    
    os.system('python c:/users/rodin/Documents/Python_Scripts/lnsum.py > c:/users/rodin/Documents/Python_Scripts/lnsum_data.dat')

def loaddat():
    
    os.chdir('c:/users/rodin/Documents/Python_Scripts')
    inline=open('c:/users/rodin/Documents/Python_Scripts/lnsum_data.dat','r')
    
    epsilon_var=[]
    exact_err=[]
    n=[]
    line=inline.readline()
    
    while bool(line):
        
        if 'epsilon:' in line:
            line=line.strip()
            tempvar=line.split(',')
            epsilon_var.append(float(tempvar[0].split(':')[-1]))
            exact_err.append(float(tempvar[1].split(':')[-1]))
            n.append(float(tempvar[-1].split('=')[-1]))
        
            print(epsilon_var,exact_err,n)
        
        line=inline.readline()
        
    inline.close()
    
    return np.array(epsilon_var), np.array(exact_err), np.array(n)

def graph(epsilon_var,exact_err,n):
    
    gs=gridspec.GridSpec(1,2,hspace=0.1)
    
    plt.subplot(gs[0])
    plt.semilogy(n,epsilon_var)
    plt.xlabel('n values')
    plt.ylabel('epsilon values')
    plt.title('Epsilon vs n curve')
    
    plt.subplot(gs[1])
    plt.semilogy(n,exact_err)
    plt.xlabel('n values')
    plt.ylabel('exact error values')
    plt.title('Exact error values vs n curve')

generate_dat()

epsilon_var, exact_err, n=loaddat()

graph(epsilon_var,exact_err,n)
    
    
        
        
        
    
    
