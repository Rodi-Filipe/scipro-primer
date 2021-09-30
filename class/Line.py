# -*- coding: utf-8 -*-
"""
Created on Thu Sep 23 17:35:02 2021

@author: rodin
"""

class Line(object):
    
    def __init__(self,p1,p2):
        
        self.p1=p1
        self.p2=p2
        self._gradient=(self.p2[1]-self.p1[1])/(self.p2[0]-self.p1[0])
    
    def value(self,x):
        
        return self._gradient*x
    
def test_Line():
    
    x=7
    p1=(0,3)
    p2=(1,8)
    
    L1=Line(p1,p2)
    f1=L1.value(7)
    f2=(p2[1]-p1[1])/(p2[0]-p1[0])*x
    
    assert abs(f1-f2)<1E-5, '%s != to %s' %(f1,f2)

if __name__ == '__main__':
    
    test_Line()