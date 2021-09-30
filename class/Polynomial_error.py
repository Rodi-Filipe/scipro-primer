# -*- coding: utf-8 -*-
"""
Created on Tue Sep 28 02:15:09 2021

@author: rodin
"""

class Polynomial(object): 
    
    def __init__(self, coefficients): 
        
        self.coeff = coefficients 
        
    def __call__(self, x): 
        
        return sum([c*x**i for i, c in enumerate(self.coeff)]) 
    
    def __add__(self, other): 
        maxlength = max(len(self.coeff), len(other.coeff)) 
        # Extend both lists with zeros to this maxlength 
        self.coeff += [0]*(maxlength - len(self.coeff)) 
        other.coeff += [0]*(maxlength - len(other.coeff)) 
        result_coeff = self.coeff 
        for i in range(maxlength): 
            result_coeff[i] += other.coeff[i] 
        return Polynomial(result_coeff)
    
poly1=Polynomial([4,5,6,7,5,30])
poly2=Polynomial([9,4,5,6])

print(poly1+poly2)