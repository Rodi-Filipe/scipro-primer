# -*- coding: utf-8 -*-
"""
Created on Sun Jul 18 17:48:19 2021

@author: rodin
"""
import sys
import numpy as np
import matplotlib.pyplot as plt
from numpy.polynomial import Polynomial

def fit(x, y, deg):
    
    plt.plot(x,y,'b-')
    plt.xlabel('Temperature')
    plt.ylabel('Density')
    plt.title('Density vs Temperature')
    plt.legend('exact')

    for i in range(len(deg)):
         coeff=Polynomial.fit(x,y,int(deg[i])).convert().coef
         ynew=np.polynomial.polynomial.polyval(x,coeff)
         plt.plot(x,ynew,linestyle='--',marker='*')
         plt.legend(['polynomial %d approximation' %deg[i]])
    plt.show()
    
def get_input():
    
    outputArg1=[]
    f_ID=open(sys.argv[1],'r')
    line=f_ID.readline()
    while line:
        tempvar=line.split()
        try: 
            if tempvar[0].count('#'):
                pass
            else:
                outputArg1.append([eval(tempvar[0]),eval(tempvar[1])])
        except:
            pass 
        line=f_ID.readline()          
    f_ID.close()
    
    return np.array(outputArg1)

data=get_input()
fit(data[:,0],data[:,1],[1,2])
    
