# -*- coding: utf-8 -*-
"""
Created on Sat Jun 19 13:32:29 2021

@author: rodin
"""

s = 0; k = 1; M = 3 
while k <= M: 
    s += 1/k 
    k += 1
print(s)

s=0
for i in range(1,M+1):
    s+=(1/i)
print(s)