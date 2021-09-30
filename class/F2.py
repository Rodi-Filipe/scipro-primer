# -*- coding: utf-8 -*-
"""
Created on Thu Sep 23 20:54:39 2021

@author: rodin
"""
import numpy as np
from math import exp, sin

class F(object):
    
    def __init__(self,a,w):
        
        self.w=w
        self.a=a
        
    def __call__(self,x):
        
        if isinstance(x,np.ndarray):
            return np.exp(-self.a*x)*np.sin(self.w*x)
        elif isinstance(x,(float,int)):
            return exp(-self.a*x)*sin(self.w*x)
        else:
            print('Invalid x value type')
    
    def __str__(self):
        
        return 'exp(-a*x)*sin(w*x)'
    
    