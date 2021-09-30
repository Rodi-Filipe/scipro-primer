# -*- coding: utf-8 -*-
"""
Created on Sat Jun 19 00:36:05 2021

@author: rodin
"""

n=100
a=1
b=90
h=(b-a)/n
vec=[]

for i in range(n+1):
    vec.append(a+i*h)
    print('%4.1f' %(vec[i]))
    

print()

vec2=[a+i*h for i in range(n+1)]
print(vec2)
    