# -*- coding: utf-8 -*-
"""
Created on Thu Sep 23 23:20:55 2021

@author: rodin
"""

class Derivative(object): 
    
    def __init__(self, f, h=1E-5): 
        self.f = f 
        self.h = float(h) 
    
    def __call__(self, x): 
        f, h = self.f, self.h # make short forms 
        return (f(x+h) - f(x))/h