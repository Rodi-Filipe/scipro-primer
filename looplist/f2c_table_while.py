# -*- coding: utf-8 -*-
"""
Created on Wed Sep 29 23:05:35 2021

@author: rodin
"""

F=[i for i in range(0,101)]

C=[(i-32)*(5/9) for i in F]

counter=0
print('   F    C')

while counter<=100:
    print('%5.1f %5.1f' %(F[counter], C[counter]))
    counter+=1