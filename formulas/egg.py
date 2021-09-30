# -*- coding: utf-8 -*-
"""
Created on Tue Jun 15 23:08:54 2021

@author: rodin
"""

from math import pi, log as ln
M=67
rho=1.038
c=3.7
K=5.48*10**-3
T_o=20
T_w=100
T_y=70

t=(M**(2/3)*c*rho**(1/3))/(K*pi**2*((4*pi)/3)**2/3)\
*ln(0.76*((T_o-T_w)/(T_y-T_w)))

print(t)
                           