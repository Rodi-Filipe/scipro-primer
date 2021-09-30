# -*- coding: utf-8 -*-
"""
Created on Sat Jun 19 19:23:17 2021

@author: rodin
"""

 
from math import sqrt 
for n in range(1, 52): 
    r = 2.0
    for i in range(n): 
        r = sqrt(r)
        print(r,'\n')
    for i in range(n): 
        r = r**2
        print(r,'\n')
    print('----------------\n\
---------------')

print ('%d times sqrt and **2: %.20f' % (n, r))