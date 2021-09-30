# -*- coding: utf-8 -*-
"""
Created on Sun Jul 25 02:08:19 2021

@author: rodin
"""

from Lagrange_poly2 import *
import numpy as np

def Ex527():
    
    for i in [2,4,6,10,13,20,30,45,50,70]:
        graph(np.abs,i,-2,2)

Ex527()