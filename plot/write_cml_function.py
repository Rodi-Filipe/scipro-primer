# -*- coding: utf-8 -*-
"""
Created on Fri Jul 16 14:30:27 2021

@author: rodin
"""
from scitools.StringFunction import StringFunction
import sys
from numpy import *

def get_input():
    
    f, a, b, n, filename=sys.argv[1:]
    
    f=StringFunction(f)
    f.vectorize(globals())
    a=eval(a)
    b=eval(b)
    n=eval(n)
        
    return f, a, b, n, filename

def write_dat(f,a,b,n,filename):
    
    x=np.linspace(a,b,n)
    y=f(x)
    
    f_ID=open('C:/Users/rodin/Documents/Python_Scripts/'+filename+'.dat','w')
    for i in range(len(x)):
        f_ID.write('%10.4f %15.4g\n' %(x[i],y[i]))
    
    f_ID.close()

f, a, b, n, filename=get_input()

write_dat(f,a,b,n,filename)

