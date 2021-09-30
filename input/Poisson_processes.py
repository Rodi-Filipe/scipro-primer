# -*- coding: utf-8 -*-
"""
Created on Thu Sep 30 14:25:12 2021

@author: rodin
"""

from math import exp, factorial

import argparse

def poisson(x, t, nu):
    
    outputArg1=((nu*t)**x/factorial(x))*exp(-nu*t)
    
    return outputArg1

def get_input():
    
    parser=argparse.ArgumentParser()
    
    parser.add_argument('--x',type=int,default='0',help='x value',metavar='x')
    parser.add_argument('--t',type=float,default='0.',help='t value',metavar='t')
    parser.add_argument('--nu',type=float,default='0.',help='nu value',metavar='nu')
    
    args=parser.parse_args()
    
    return args.x, args.t, args.nu

def solvefunc():
    
    x, t, nu=get_input()

    print(poisson(x,t,nu)*100)

solvefunc()

"""
runfile('Possion_processes.py', wdir='C:/Users/rodin/Documents/Python Scripts',args='--x 0 --t 0.5 --nu 5')
0.0820849986238988

runfile('Possion_processes.py', wdir='C:/Users/rodin/Documents/Python Scripts',args='--x 0 --t 2 --nu 5')
4.5399929762484854e-05

runfile('Possion_processes.py', wdir='C:/Users/rodin/Documents/Python Scripts',args='--x 2 --t 0.33 --nu 5')
0.26142793811000153

runfile('Possion_processes.py', wdir='C:/Users/rodin/Documents/Python Scripts',args='--x 2 --t 0.33 --nu 5')
26.142793811000153

runfile('Possion_processes.py', wdir='C:/Users/rodin/Documents/Python Scripts',args='--x 2 --t 0.33 --nu 5')
26.142793811000153

runfile('Possion_processes.py', wdir='C:/Users/rodin/Documents/Python Scripts',args='--x 3 --t 10 --nu 0.3')
22.404180765538776

runfile('Possion_processes.py', wdir='C:/Users/rodin/Documents/Python Scripts',args='--x 0 --t 0.0192307692 --nu 0.2')
99.61612331361636
"""