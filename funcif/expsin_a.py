# -*- coding: utf-8 -*-
"""
Created on Thu Jun 24 18:56:47 2021

@author: rodin
"""

from math import e, pi, sin

g = lambda x, a: e**(-a*x)*sin(pi*x)

print(g(0,10),g(1,10))