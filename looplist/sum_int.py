# -*- coding: utf-8 -*-
"""
Created on Fri Jun 18 23:03:48 2021

@author: rodin
"""

n=100
runsum=0

for i in range(1,n+1):
    runsum+=i
    print(runsum)

print()
print(runsum, n*(n+1)/2)    
