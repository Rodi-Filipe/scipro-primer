# -*- coding: utf-8 -*-
"""
Created on Tue Jun 29 13:57:34 2021

@author: rodin
"""

import sys

def L3_ci(x, epsilon=1.0E-6): 
    i = 1
    term = (1.0/i)*(x/(1+x))**i 
    s = term 
    while abs(term) > epsilon:  
        i+=1
        term *= ((i-1)*x)/(i*x+i)
        s += term 
    return s, i

def L3(x, epsilon=1.0E-6):
    i = 1 
    term = (1.0/i)*(x/(1+x))**i 
    s = term 
    while abs(term) > epsilon: 
        i += 1 
        term = (1.0/i)*(x/(1+x))**i 
        s += term 
    return s, i

def test_L3_ci():   
    x = eval(sys.argv[1])
    exact = L3(x)
    print(exact)
    expct = L3_ci(x)
    print(expct)
    success1 = abs(exact[0]-expct[0]) < 1e-13
    success2 = exact[1]==expct[1]
    msg1 = 'test failed! %4.2f (exact) != to %4.2f (expected)' %(exact[0], expct[0])
    msg2 = 'test failed! %4.2f (exact) != to %4.2f (expected)' %(exact[1], expct[1])
    assert success1, msg1
    assert success2, msg2

test_L3_ci()