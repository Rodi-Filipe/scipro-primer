# -*- coding: utf-8 -*-
"""
Created on Thu Sep 23 18:07:55 2021

@author: rodin
"""

class Line(object):
    
    def __init__(self,p1,p2):
        
        self.p1=p1
        self.p2=p2
    
    def value(self,x):
       
        if isinstance(self.p1,(tuple, list)) and isinstance(self.p2,(tuple, list)):    
            return (self.p2[1]-self.p1[1])/(self.p2[0]-self.p1[0])*x
        elif isinstance(self.p1,(tuple,list)) and isinstance(self.p2,(float,int)):
            c=self.p1[1]-self.p1[0]*self.p2
            return self.p2*x+c
        elif isinstance(self.p1,(float,int)) and isinstance(self.p2,(float,int)):
            return self.p1*x+self.p2
        else:
            print('Invalid data attribute types')
    
def test_Line():
    
    x=7
    p1=(0,3)
    p2=10
    
    L1=Line(p1,p2)
    f1=L1.value(7)
    f2=p2*x+(p1[1]-p2*p1[0])
    
    assert abs(f1-f2)<1E-5, '%s != to %s' %(f1,f2)

if __name__ == '__main__':
    
    test_Line()