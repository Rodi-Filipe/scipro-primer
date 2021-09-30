# -*- coding: utf-8 -*-
"""
Created on Tue Jun 15 22:39:50 2021

@author: rodin
"""

from math import pi

C_d=0.4
rho=1.2 #kg*m^-3
r=11*10**-2 #m
A=pi*(r)**2 #m^2
V=30*(1000/3600) #m/s
m=0.43 #Kg
g=9.81 #m/s^2

F_d=(1/2)*C_d*rho*A*V**2

F_g=m*g

print('\nDrag Force:', F_d, ', Gravitational Force:', F_g)
