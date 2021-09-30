# -*- coding: utf-8 -*-
"""
Created on Sat Mar 13 16:30:34 2021

@author: rodin
"""
metre_val=640

inches = (25196.85*(metre_val))/640 

feet = (2099.74*(metre_val))/640

yards = (699.91*(metre_val))/640

miles = (0.3977*(metre_val))/640

print('\nA value of %g corresponds to\n\
%g inches, %g feet, %g yards, and\n\
%g miles' %(metre_val, inches, feet, yards, miles))
 
