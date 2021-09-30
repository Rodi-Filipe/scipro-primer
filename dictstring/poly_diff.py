# -*- coding: utf-8 -*-
"""
Created on Sat Sep 11 04:09:29 2021

@author: rodin
"""

def diff(dict_var):
    
    outputArg1={}
    for coeff in dict_var:
        
        if coeff != 0:
            outputArg1[coeff-1]=coeff*dict_var[coeff]
    
    return outputArg1


def main():
    
    p = {0: -3, 3: 2, 5: -1}
    
    print(diff(p))
   
   
main()
    