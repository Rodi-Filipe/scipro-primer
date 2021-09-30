# -*- coding: utf-8 -*-
"""
Created on Wed Sep 29 02:08:58 2021

@author: rodin
"""

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
    
    def __sub__(self,other):
        
         maxlength = max(len(self.coeff), len(other.coeff))
         # Extend both lists with zeros to this maxlength
         self.coeff += [0]*(maxlength - len(self.coeff)) 
         other.coeff += [0]*(maxlength - len(other.coeff))
         result_coeff = self.coeff
         
         for i in range(maxlength):
             result_coeff[i] -= other.coeff[i]
         return Polynomial(result_coeff)
         
def test_Polynomial():
    
    coeff1=[10, 0, 1]
    coeff2=[8, 1, 5, 4]
    
    poly1=Polynomial(coeff1)
    poly2=Polynomial(coeff2)
    
    result=poly1-poly2
    exact=[2, -1, -4, -4]
    
    assert result.coeff==exact, 'Test failed!, %s != to %s' %(result.coeff,exact)

if __name__ == '__main__':
    
    test_Polynomial()
    