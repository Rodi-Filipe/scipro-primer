# -*- coding: utf-8 -*-
"""
Created on Thu Jun 24 19:05:29 2021

@author: rodin
"""

C = lambda F: (5/9)*(F-32)

F = lambda C: (9/5)*(C)+32


c=38
f=78

print(C(F(c)))
print(F(C(f)))

