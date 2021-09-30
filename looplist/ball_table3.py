# -*- coding: utf-8 -*-
"""
Created on Sat Jun 19 18:15:27 2021

@author: rodin
"""

v_o=50
g=9.81

n=50
a=0
b=(2*(v_o/g))
h=(b-a)/(n-1)
t=[0]*n
y=[0]*n

for i in range(n):
    t[i]=a+(i+1)*h
    y[i]=v_o*t[i]-0.5*g*t[i]**2

ty1=[t, y]

print('\n   t       y(t)')
for j in range(len(t)):
    print('%5.2f' % t[j], end=' ')
    print('%9.2f' % y[j])
  
ty2=[0]*n
for i in range(n):
    t[i]=a+(i+1)*h
    y[i]=v_o*t[i]-0.5*g*t[i]**2
    ty2[i]=[t[i], y[i]]

print('\n    t      y(t)')
for j in ty2:
    for i in range(len(j)):
        print('%7.2f' % j[i], end=' ')
    print()
    
    
    