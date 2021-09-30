# -*- coding: utf-8 -*-
"""
Created on Sat Jun 26 22:22:44 2021

@author: rodin
"""

def  polygon_area(x,y):
    
    runsum1=0
    for i in range(len(x)):
        if i==len(x)-1:
            runsum1+=(x[i]*y[0])
        else:
            runsum1+=(x[i]*y[i+1])
    
    runsum2=0
    for i in range(len(y)):
        if i==len(x)-1:
            runsum2+=(y[i]*x[0])
        else:
            runsum2+=(y[i]*x[i+1])
            
    return 0.5*abs(runsum1-runsum2)


x=[0,2,6,12,5,2]

y=[0,9,10,20,8,2]

print(polygon_area(x,y))