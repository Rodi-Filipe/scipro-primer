# -*- coding: utf-8 -*-
"""
Created on Thu Jul  8 23:55:35 2021

@author: rodin
"""

from math import pi

import argparse

import sinesum2 

def get_input():
    
    parser=argparse.ArgumentParser()
    
    parser.add_argument('--n',type=str,default='',help='n values',metavar='n')
    parser.add_argument('--a',type=str,default='',help='alpha values',metavar='a')
    parser.add_argument('--T',type=str,default='',help='period value',metavar='T')

    args=parser.parse_args()

    args.n=eval(args.n)
    args.a=eval(args.a)
    args.T=eval(args.T)
    
    return args.n, args.a, args.T  

n, a, T=get_input()

sinesum2.table(n, a, T)