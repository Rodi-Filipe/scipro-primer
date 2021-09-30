# -*- coding: utf-8 -*-
"""
Created on Sun Sep 12 23:44:14 2021

@author: rodin
"""

import sys
from scitools.StringFunction import StringFunction
from math import sin

def get_func1():
    
    if len(sys.argv[1:])!=1:
        if not('with parameter' in sys.argv[1:]):
            f=eval('StringFunction(sys.argv[1],independent_variables=sys.argv[5])')
        else:
            f=eval('StringFunction(sys.argv[1],independent_variables=sys.argv[5], %s)' % sys.argv[8])
    elif len(sys.argv[1:])==1:
        if not('with parameter' in sys.argv[1]):
            f=eval('StringFunction(sys.argv[1][0],independent_variables=sys.argv[1][4])')
        else:
            f=eval('StringFunction(sys.argv[1].split(' ')[0],independent_variables=sys.argv[1].split("is a function of ")[-1][0], %s)' % sys.argv[1].split('with parameter')[-1])
    
    return f

def get_func2():
    
    if len(sys.argv[1:])!=1:
        str_var=' '.join(sys.argv[1:])
    else:
        str_var=sys.argv[1]
    
    func, rest = str_var.split('is a function of ')
    x, params = rest.split('with parameter')
    x=x.strip()
    params=params.strip()
    f=eval('StringFunction(func,independent_variables=x.strip("[,]"), %s)' %params)        
    
    return f    
        
print(get_func1())

print(get_func2())

print('sin(x) is a function of x'.split('with parameter'))
