# -*- coding: utf-8 -*-
"""
Created on Sun Aug 29 21:32:41 2021

@author: rodin
"""

from collections import defaultdict

def create_dat():
    
    poly_list=[0]*101
    poly_list[0]=-0.5
    poly_list[-1]=2
    
    poly_dict=defaultdict(float)
    
    poly_dict.update({0: -0.5, 100: 2})
    
    return poly_list, poly_dict

def eval_poly_dict2(poly, x): 
    
    return sum(poly[power]*x**power for power in poly)

def eval_poly_list(poly, x): 
    
    sum = 0 
    for power in range(len(poly)): 
        sum += poly[power]*x**power 
    return sum

poly_list, poly_dict=create_dat()

print(eval_poly_dict2(poly_dict, 7))

print(eval_poly_list(poly_list, 7))
    
    

    
    