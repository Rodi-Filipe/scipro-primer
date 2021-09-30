# -*- coding: utf-8 -*-
"""
Created on Sat Jun 26 14:27:53 2021

@author: rodin
"""


def trapezint1(f,a,b):
    
    return ((b-a)/2)*(f(a)+f(b))



from math import cos, pi, sin

f1=lambda x: cos(x)
f2=lambda x: sin(x)



print(trapezint1(f1,0,pi), abs(0-trapezint1(f1,0,pi)))
print(trapezint1(f2, 0, pi), abs(2-trapezint1(f2, 0, pi)))
print(trapezint1(f2, 0, pi/2), abs(1-trapezint1(f2, 0, pi/2)))
