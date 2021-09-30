# -*- coding: utf-8 -*-
"""
Created on Mon Sep 27 02:24:35 2021

@author: rodin
"""

import sys
from math import factorial, exp

class Polynomial(object): 
    
    def __init__(self, coefficients): 
        self.coeff = coefficients 
        
    def __call__(self, x): 
        
        """Evaluate the polynomial.""" 
        s = 0 
        for i in range(len(self.coeff)): 
            s += self.coeff[i]*x**i 
        return s 
    
    def __add__(self, other): 
        
        """Return self + other as Polynomial object.""" 
        # Two cases: # # self: XXXXXXX 
        # other: X X X # # or: 
        # # self: XXXXX 
        # other: XXXXXXXX 
        # Start with the longest list and add in the other 
        if len(self.coeff) > len(other.coeff): 
            result_coeff = self.coeff[:] # copy! 
            for i in range(len(other.coeff)):
                result_coeff[i] += other.coeff[i] 
        else: 
            result_coeff = other.coeff[:] # copy!
            for i in range(len(self.coeff)): 
                result_coeff[i] += self.coeff[i] 
        
        return Polynomial(result_coeff)

def main():
    
    x=eval(sys.argv[1])
    N_values=[eval(value) for value in sys.argv[2:]]
    
    for N_value in N_values:
        Tp=Polynomial([ 1/factorial(k) for k in range(N_value+1)])
        print(Tp(x), exp(x))

main()
        
