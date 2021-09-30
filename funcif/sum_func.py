# -*- coding: utf-8 -*-
"""
Created on Sat Jun 26 00:32:55 2021

@author: rodin
"""

def sum_1k(M):
    
    s=0

    for i in range(1,M+1):
        s+=1/i
    
    return s



def test_sum_1k():
    
    exact=11/6
    
    expected=sum_1k(3)
    
    output=abs(exact-expected) < 1e-20
    
    msg='test failed'
    
    assert output, msg


test_sum_1k()