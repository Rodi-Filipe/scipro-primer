# -*- coding: utf-8 -*-
"""
Created on Sun Aug 29 21:28:08 2021

@author: rodin
"""


def triangle_area(vertices):
    
    term1=vertices[2][0]*vertices[3][1]
    term2=vertices[3][0]*vertices[2][1]
    term3=vertices[1][0]*vertices[3][1]
    term4=vertices[3][0]*vertices[1][1]
    term5=vertices[1][0]*vertices[2][1]
    term6=vertices[2][0]*vertices[1][1]
    return 0.5*abs(term1-term2-term3+term4+term5-term6)

def test_triangle_area(): 
    """ 
    Verify the area of a triangle with vertex coordinates (0,0), (1,0), and (0,2). 
    """ 
    vertices={1: (0,0), 2: (1,0), 3: (0,2)} 
    expected = 1 
    computed = triangle_area(vertices) 
    tol = 1E-14 
    success = (expected - computed) < tol 
    msg = 'computed area=%g != %g (expected)' % (computed, expected) 
    assert success, msg
    
test_triangle_area()
