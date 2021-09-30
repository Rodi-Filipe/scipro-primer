# -*- coding: utf-8 -*-
"""
Created on Thu Jun 24 19:19:05 2021

@author: rodin
"""

def double(inputArg1):
    return inputArg1*2


def test_double(): 
    assert double(2) == 4
    assert abs(double(0.1) - 0.2) < 1E-15 
    assert double([1, 2]) == [1, 2, 1, 2] 
    assert double((1, 2)) == (1, 2, 1, 2) 
    assert double(3+4j) == 6+8j 
    assert double('hello') == 'hellohello'



test_double()
