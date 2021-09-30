# -*- coding: utf-8 -*-
"""
Created on Wed Jul  7 18:52:07 2021

@author: rodin 

￼
"""

import sys

def C2F(c):
    
    outputArg1=(c*(9/5))+32
    
    return outputArg1

def F2C(f):
    
    outputArg1=(f-32)*(5/9)
    
    return outputArg1

def C2K(c):
    
    outputArg1=c+273.15
    
    return outputArg1

def K2C(k):
    
    outputArg1=k-273.15
    
    return outputArg1

def F2K(f):
    
    outputArg1=(f-32)*(5/9)+273.15
    
    return outputArg1

def K2F(k):
    
    outputArg1=(k-273.15)*(9/5)+32
    
    return outputArg1

def test_conversion():
    
    tol=1E-5
    c=31
    f=89
    success1=abs(f-C2F(F2C(f)))<tol
    success2=abs(c-K2C(C2K(c)))<tol
    success3=abs(f-K2F(F2K(f)))<tol
    
    msg1='test failed %5.2f != to %5.2f' %(f, C2F(F2C(c)))
    msg2='test failed %5.2f != to %5.2f' %(c, K2C(C2K(c)))
    msg3='test failed %5.2f != to %5.2f' %(f, K2F(F2K(f)))
    
    assert success1, msg1
    assert success2, msg2
    assert success3, msg3


if __name__=='__main__':
    if len(sys.argv)==2 and sys.argv[1]=='verify':
        test_conversion()
    elif len(sys.argv)==3 and sys.argv[2]=='C':
        print('F=',C2F(eval(sys.argv[1])),'K=',C2K(eval(sys.argv[1])))
    elif len(sys.argv)==3 and sys.argv[2]=='F':
        print('C=',F2C(eval(sys.argv[1])),'K=',F2K(eval(sys.argv[1])))
    elif len(sys.argv)==3 and sys.argv[2]=='K':
        print('C=',K2C(eval(sys.argv[1])),'F=',K2F(eval(sys.argv[1])))
    else:
        print('Invalid command line argments or no command line arguments given')        
    

__all__=['C2F','F2C','C2K','K2C','F2K','K2F']
