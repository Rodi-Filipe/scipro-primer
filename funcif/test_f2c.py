# -*- coding: utf-8 -*-
"""
Created on Sat Jun 26 00:15:56 2021

@author: rodin
"""

C = lambda F: (5/9)*(F-32)

F = lambda C: (9/5)*(C)+32


def test_f2c():
    
    c=38
    f=78
    
    result1=abs(c-C(F(c))) < 1e-13

    result2=abs(f-F(C(f))) < 1e-11

    msg_1='test %d failed' %(1)

    msg_2='test %d failed' %(2)

    assert result1, msg_1
    assert result2, msg_2
    
test_f2c()