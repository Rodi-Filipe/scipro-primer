# -*- coding: utf-8 -*-
"""
Created on Tue Jun 15 22:09:44 2021

@author: rodin
"""

a = 3.3; b = 5.3; a2 = a**2; b2 = b**2
eq1_sum = a2 + 2*a*b + b2 
eq2_sum = a2 - 2*a*b + b2 
eq1_pow = (a + b)**2 
eq2_pow = (a - b)**2
 
print('First equation: %g = %g' %(eq1_sum, eq1_pow)) 
print ('Second equation: %g = %g' %(eq2_pow, eq2_pow))