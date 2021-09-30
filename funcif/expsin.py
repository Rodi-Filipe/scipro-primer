# -*- coding: utf-8 -*-
"""
Created on Thu Jun 24 18:53:53 2021

@author: rodin
"""

from math import e, pi, sin

g = lambda x: e**(-x)*sin(pi*x)

print(g(0),g(1))
 