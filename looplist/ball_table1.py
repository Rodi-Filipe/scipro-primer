# -*- coding: utf-8 -*-
"""
Created on Sat Jun 19 00:50:50 2021

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


print('\n   t       y(t)')
for i in range(n):
    t[i]=a+(i+1)*h
    y[i]=v_o*t[i]-0.5*g*t[i]**2
    print('%7.3f %7.1f' %(t[i], y[i]))


counter=0
print('\n\n\n   t        y(t)')
while counter<n:
    t[counter]=a+(counter+1)*h
    y[counter]=v_o*t[counter]-0.5*g*t[counter]**2
    print('%7.3f %8.1f' %(t[counter], y[counter]))
    counter+=1
    
counter=0
print('\n\n\n   t        y(t)')
while counter<n:
    counter+=1
    t[counter-1]=a+(counter)*h
    y[counter-1]=v_o*t[counter-1]-0.5*g*t[counter-1]**2
    print('%7.3f %8.1f' %(t[counter-1], y[counter-1]))
