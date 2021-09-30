# -*- coding: utf-8 -*-
"""
Created on Sun Sep 26 17:39:51 2021

@author: rodin
"""

import sympy

class Central(object):
    
    def __init__(self,f,h=1E-4):
        
        self.prop1=f
        self.prop2=h
        
    def __call__(self,x):
        
        outputArg1=(self.prop1(x+self.prop2)-self.prop1(x-self.prop2))/(2*self.prop2)
        
        return outputArg1

def test_Central():
    
    x=4
    f=lambda x: x**2-4*x-10
    
    c1=Central(f)
    df=lambda x: 2*x-4
    
    assert abs(c1(x)-df(x))<1E-9, 'Test failed!, %s != to %s' %(c1(x)-df(x))
    
def f(x): 
    
    return 0.25*x**4 

def table(f, x, h=1E-5):
    
    x_sym = sympy.Symbol('x')
    y=sympy.lambdify([x_sym], f)
    c1=Central(y,h)
    
    df=sympy.diff(f)
    df=sympy.lambdify([x_sym],df)
    
    for xvalue in x:
        print('%9.4f %9.4f %14.10f' %(c1(xvalue),df(xvalue),abs(c1(xvalue)-df(xvalue))))
        
    
if __name__ == '__main__':
    
    test_Central()

    df = Central(f) # make function-like object df
    # df(x) computes the derivative of f(x) approximately 
    x = 2 
    print('df(%g)=%g' % (x, df(x)))
    print('exact:', x**3)

    table('x*sin(2*x)',[i for i in range(100+1)])


        