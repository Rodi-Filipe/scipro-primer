# -*- coding: utf-8 -*-
"""
Created on Fri Jul  9 00:40:22 2021

@author: rodin
"""

import subprocess

import os

from math import exp, log as ln, sin, cos

import random

def power3_identity(A=-100, B=100, n=1000):
    
    runsum=0
    for i in range(n):
        a=random.uniform(A,B)
        b=random.uniform(A,B)
        
        if (a*b)**3 == a**3*b**3:
            runsum+=1
    
    return (runsum/n)*100

def equal(expr1, expr2, A=1, B=100, n=500):
    
    runsum=0
    for i in range(n):
        a=random.uniform(A,B)
        b=random.uniform(A,B)
        
        if eval(expr1) == eval(expr2):
            runsum+=1
    
    return (runsum/n)*100

def equal_v1(exprlist,A=1,B=100,n=1000):
    
   f_ID =open('Ex4.23.dat','w')
   for expr in exprlist:
        runsum=0
        for i in range(n):
            a=random.uniform(A,B)
            b=random.uniform(A,B)
        
            if eval(expr[0]) == eval(expr[1]):
                runsum+=1
        f_ID.write('%30s %30s %10.2f\n' %(expr[0], expr[1], (runsum/n)*100))
   f_ID.close()


exprlist=[('a-b','-(b-a)'),('a/b','1/(b/a)'),('(a*b)**4','a**4*b**4'),\
          ('(a+b)**2','a**2+2*a*b+b**2'),('(a+b)*(a-b)','a**2-b**2'),('a*(sin(b)**2+cos(b)**2)','a')]

print(power3_identity())
print(equal('ln(a**b)','b*ln(a)'))
equal_v1(exprlist)
