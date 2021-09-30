# -*- coding: utf-8 -*-
"""
Created on Mon Jul  5 11:10:38 2021

@author: rodin
"""

import sys

def get_input():
    
    if isinstance(sys.argv[1],str):
        outputArg1=sys.argv[1]
    else:
        outputArg1=eval(sys.argv[1])
            
    return outputArg1
#
def input_process(inputArg1):
    
    print(inputArg1,type(inputArg1))
    

var=get_input()

input_process(var)
