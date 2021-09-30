# -*- coding: utf-8 -*-
"""
Created on Thu Sep 23 22:30:51 2021

@author: rodin
"""
from math import factorial,pi
class Sum(object):
    
    def __init__(self,term,M,N):
        
        self.term=term 
        self.M=M
        self.N=N
        
    def __call__(self,x):
        
       outputArg1=sum([self.term(k,x) for k in range(self.M,self.N+1)])
       
       return outputArg1
   
def term (k, x):
    
    return (-x)**k 

def test_Sum():
    
    x=1
    S=Sum(term,1,100)
    
    r1=S(x)
    r2=sum([(-x)**k for k in range(1,100+1)])

    assert abs(r1-r2)<1E-5, 'Test failed!, %.4f != to %.4f' %(r1,r2)

test_Sum()
S = Sum(term, M=0, N=3) 
x = 0.5 
print(S(x)) 
print(S.term(k=4, x=x)) # (-0.5)**4

#Taylor polynomial approximation of sin(x)

S=Sum(lambda k, x: ((-1)**(k+2))*(x**(2*k+1)/factorial(2*k+1)),0,50)
x=pi
print('%.5F' %S(x))