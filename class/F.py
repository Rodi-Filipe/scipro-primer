# -*- coding: utf-8 -*-
"""
Created on Fri Sep 17 16:42:13 2021

@author: rodin
"""

from math import exp, sin

class F(object):
    
    def __init__(self,a,w):
        
        self.a=a
        self.w=w
    
    def value(self,x):
        
        return exp(-self.a*x)*sin(self.w*x)

