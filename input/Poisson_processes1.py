# -*- coding: utf-8 -*-
"""
Created on Sat Jul 10 20:15:56 2021

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
