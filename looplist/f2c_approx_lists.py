# -*- coding: utf-8 -*-
"""
Created on Sat Jun 19 14:58:40 2021

@author: rodin
"""

F=[i for i in range(0,101)]

C=[(i-32)*(5/9) for i in F]

Capprox=[(i-30)/2 for i in F]

conversion=[]

print('\n    F       C    Capprox')
for i in range(len(F)):
    conversion.append([F[i], C[i], Capprox[i]])
    print('%7.2f' %(F[i]),end=' ')
    print('%7.2f' %(C[i]),end=' ')
    print('%7.2f' %(Capprox[i]))


    