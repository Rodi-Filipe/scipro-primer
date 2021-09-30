# -*- coding: utf-8 -*-
"""
Created on Wed Aug 25 01:01:05 2021

@author: rodin
"""

import urllib.request as urllibr
import pprint
import os



def loaddat():
    
    urllibr.urlretrieve('https://raw.githubusercontent.com/hplgit/scipro-primer/master/src/dictstring/constants.txt',filename='c:/users/rodin/Documents/Python_Scripts/constants.txt')
    os.chdir('C:/users/rodin/Documents/Python_Scripts')
    f_ID=open('constants.txt','r')
    
    f_ID.readline()
    f_ID.readline()
    
    constants={}
    
    for line in f_ID:
        tempvar=line.split()
        constants[' '.join(tempvar[0:-2])]=float(tempvar[-2])
    
    f_ID.close()
    
    pprint.pprint(constants)
    
    return constants

constants=loaddat()
        