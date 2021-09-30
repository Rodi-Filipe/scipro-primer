# -*- coding: utf-8 -*-
"""
Created on Sat Jun 19 12:50:14 2021

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
 
print('\n   t       y(t)')
for i in range(len(y)):
    print('%7.3f' % t[i], end=' ')
    print('%7.1f' % y[i],)

print('\n\n\n')
print('    t      y(t)')
for i,j in zip(t, y):
    print('%7.3f %7.1f' %(i, j))
    
