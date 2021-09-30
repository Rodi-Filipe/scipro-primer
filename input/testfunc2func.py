# -*- coding: utf-8 -*-
"""
Created on Tue Jul  6 21:40:32 2021

@author: rodin
"""

def halve(x):
    
    if isinstance(x,float):
        outputArg1=x/2
    else:
        outputArg1=x//2
        
    return outputArg1

def add(a,b):
    
    return a+b

def equal(a,b):
    
    strvar=''
    if a == b:
        return True, a
    elif len(a)<len(b):
        for i in range(len(b)):
            try:
                if a[i]==b[i]:
                    strvar+=a[i]
                else:
                    strvar+=a[i]+'|'+b[i]
            except IndexError:
                strvar+='*|'+b[i]
    elif len(a)>len(b):
         for i in range(len(a)):
             try:
                 if a[i]==b[i]:
                    strvar+=a[i]
                 else:
                    strvar+=a[i]+'|'+b[i]
             except IndexError:
                strvar+=a[i]+'|*'
    else:
        for i in range(len(a)):
            if a[i]==b[i]:
                strvar+=a[i]
            else:
                strvar+=a[i]+'|'+b[i]
    return False, strvar

def test_halve(): 
    assert halve(5.0) == 2.5 # Real number division 
    assert halve(5) == 2 # Integer division
 
def test_add():
    # Test integers 
    assert add(1, 2) == 3 
    
    # Test floating-point numbers with rounding error 
    tol = 1E-14 
    a = 0.1; b = 0.2 
    computed = add(a, b) 
    expected = 0.3 
    assert abs(expected - computed) < tol 
    
    # Test lists 
    assert add([1,4], [4,7]) == [1,4,4,7] 
    
    # Test strings 
    assert add('Hello, ', 'World!') == 'Hello, World!'

def test_equal(): 
    assert equal('abc', 'abc') == (True, 'abc') 
    assert equal('abc', 'aBc') == (False, 'ab|Bc') 
    assert equal('abc', 'aBcd') == (False, 'ab|Bc*|d')
    assert equal('Hello, World!', 'hello world') == (False, 'H|hello,|  |wW|oo|rr|ll|dd|*!|*') 
 
              
test_halve()

test_add()

test_equal() 

print(equal('Hello, World!', 'hello world'))