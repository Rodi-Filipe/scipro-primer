# -*- coding: utf-8 -*-
"""
Created on Sun Sep 26 19:06:37 2021

@author: rodin
"""

from math import sin, pi, cos

class Derivative(object): 
    
    def __init__(self, f, h=1E-5): 
        self._f = f 
        self._h = float(h) 
        
    def __call__(self, x): 
        
        f, h = self._f, self._h # make short forms 
        return (f(x+h) - f(x))/h
    
    def get_precision(self):
        
        return self._h
    
    def set_precision(self,value):
        
        self._h=value

class Derivative1(object):
    
    tempvar=0
    
    def __init__(self,f,h=1E-5):
        
        Derivative1.tempvar+=2
        self.f = f
        self.h = float(h)
        
    @property
    def f(self):
        if Derivative1.tempvar>0:
            Derivative1.tempvar-=1
            return self._f
        else:
            return 'Private Attribute! Access denied'
            raise AttributeError('Private Attribute! Access denied')
    
    @f.setter
    def f(self,value):
        if Derivative1.tempvar>0:
            Derivative1.tempvar-=1
            self._f=value
        else:
            return 'Private Attribute! Access denied'
            raise AttributeError('Private Attribute! Access denied')
    
    @property
    def h(self):
        if Derivative1.tempvar>0:
            Derivative1.tempvar-=1
            return self._h
        else:
            return 'Private Attribute! Access denied'
            raise AttributeError('Private Attribute! Access denied')
    
    @h.setter
    def h(self,value):
        if Derivative1.tempvar>0:
            Derivative1.tempvar-=1
            self._h=value
        else:
            return 'Private Attribute! Access denied'
            raise AttributeError('Private Attribute! Access denied')
    
    def __call__(self, x):
        
        Derivative1.tempvar+=2
        f, h = self.f, self.h # make short forms 
        return (f(x+h) - f(x))/h

def test_Derivative1():
    
    dsin=Derivative1(lambda x: sin(x))
    msg1=dsin.f
    msg2=dsin.h
    
    success='Private Attribute! Access denied'==msg1 and 'Private Attribute! Access denied'==msg2\
        and abs(cos(pi)-dsin(pi))<1E-5
    
    assert success, 'Test failed!'
    
if __name__ == '__main__':
    
    test_Derivative1()