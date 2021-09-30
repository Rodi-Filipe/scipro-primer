# -*- coding: utf-8 -*-
"""
Created on Thu Aug 26 03:00:02 2021

@author: rodin
"""

import urllib.request as urllibr
import os
import pprint
import math

def readdat():
    
    urllibr.urlretrieve('https://raw.githubusercontent.com/hplgit/scipro-primer/master/src/funcif/stars.txt',filename='c:/users/rodin/Documents/Python_Scripts/stars.txt')
    inline=open('stars.txt','r')
    
    data={}
    line=inline.readline()
    
    while bool(line):
        if '(' in line:
            line=line.strip('(,\n)')
            tempvar=line.split(',')
            data[tempvar[0][1:-1]]={}
            data[tempvar[0][1:-1]]['distance']=float(tempvar[1])
            data[tempvar[0][1:-1]]['brightness']=float(tempvar[2])
            data[tempvar[0][1:-1]]['luminosity']=float(tempvar[-1])
        
        line=inline.readline()
    
    inline.close()
    
    return data

data=readdat()

pprint.pprint(data)