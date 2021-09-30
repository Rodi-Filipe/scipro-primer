# -*- coding: utf-8 -*-
"""
Created on Thu Sep 23 23:38:00 2021

@author: rodin
"""

class rope(object):
    
    def __init__(self,inputArg1):
        
        self.knots=inputArg1
        
    def __add__(self,other):
        
        return rope(self.knots + other.knots + 1)
    
    def __radd__(self,other):
        
        return rope(self.__add__(other))
    
    def __str__(self):
        
        return '%.2f' %self.knots if isinstance(self.knots,float) else '%d' %self.knots
    
def test_rope():
    
    outputArg1=rope(4)+rope(20)
    outputArg2=4+20+1
    
    assert abs(outputArg1.knots-outputArg2)<1E-5, 'Test failed!, %s != to %s' %(outputArg1.knots, outputArg2)
    
if __name__ == '__main__':
    
    test_rope()
    