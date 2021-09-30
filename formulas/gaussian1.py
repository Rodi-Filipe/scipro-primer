# -*- coding: utf-8 -*-
"""
Created on Tue Jun 15 22:20:17 2021

@author: rodin
"""

from math import pi, exp, sqrt
m=0
s=2
x=1

f=(1/(sqrt(2*pi)*s))*exp(-1/2*((x-m)/s)**2)

print(f)