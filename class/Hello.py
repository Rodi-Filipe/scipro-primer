# -*- coding: utf-8 -*-
"""
Created on Thu Sep 23 21:15:49 2021

@author: rodin
"""

class Hello(object):
    
    def __init__(self):
        
        self.prop='Hello, World!'
    
    def __call__(self,value):
        
        return 'Hello' + ' ' + value + '!'
    
    def __str__(self):
        
        return self.prop
    
    
        