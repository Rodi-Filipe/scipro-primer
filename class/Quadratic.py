# -*- coding: utf-8 -*-
"""
Created on Fri Sep 17 23:47:21 2021

@author: rodin
"""

from numpy import roots, polyval

class Quadratic(object):
    
    def __init__(self,a,b,c):
        
        self.a=a
        self.b=b
        self.c=c
    
    def values(self,x):
        
        return polyval([self.a, self.b, self.c],x)
    
    def table(self,l,r,n):
        
        mat=[[k,self.values(k)] for k in range(n+1)]
        print('   x    ','    f(x)',sep=' ')
        
        for i in range(len(mat)):
            print('%8.4g %8.4g' %(mat[i][0],mat[i][1]))
    
    def roots(self):
        
        return roots([self.a, self.b, self.c])

def test_Quadratic():
    
    a=3
    b=4
    c=1
    Q1=Quadractic(a,b,c)
    
    f1=Q1.values(5)
    f2=polyval([a,b,c],5)
    
    r1=Q1.roots()
    r2=roots([a,b,c])
    
    assert abs(f1-f2).max()<1E-5, '%s != to %s' %(f1, f2)
    assert abs(r1-r2).max()<1E-5, '%s != to %s' %(r1, r2)

if __name__ == '__main__':
    test_Quadratic()