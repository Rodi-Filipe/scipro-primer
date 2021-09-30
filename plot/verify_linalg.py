# -*- coding: utf-8 -*-
"""
Created on Sat Aug 21 02:48:28 2021

@author: rodin
"""

import numpy as np

def test_oper1():
    
    n = 4 # matrix size
    A = np.matrix(np.random.rand(n, n))
    B = np.matrix(np.random.rand(n, n))
    C = np.matrix(np.random.rand(n, n))


    tol = 1E-4
    result1 = (A+B)*C
    result2 = A*C + B*C
    
    assert abs(result1-result2).max() < tol

def test_oper2():
    
    n = 4 # matrix size
    A = np.matrix(np.random.rand(n, n))
    B = np.matrix(np.random.rand(n, n))
    C = np.matrix(np.random.rand(n, n))
    
    tol = 1E-4
    result1 = (A*B)*C
    result2 = A*(B*C)
    
    assert abs(result1-result2).max() < tol
    
def test_oper3():
    
    n = 4 # matrix size
    A = np.matrix(np.random.rand(n, n))
    
    tol = 1E-4
    result1 = np.linalg.matrix_rank(A)
    result2 = np.linalg.matrix_rank(A.T)
    
    assert abs(result1-result2).max() < tol
    
def test_oper4():
    
    n = 4 # matrix size
    A = np.matrix(np.random.rand(n, n))
    B = np.matrix(np.random.rand(n, n))
    
    tol = 1E-4
    result1 = np.linalg.det(A*B)
    result2 = np.linalg.det(A)*np.linalg.det(B)
    
    assert abs(result1-result2).max() < tol
    
def test_oper5():
    
    n = 4 # matrix size
    A = np.matrix(np.random.rand(n, n))
    
    tol = 1E-4
    result1 = np.linalg.eig(A)[-1]
    result2 = np.linalg.eig(A.T)[-1]
    
    assert abs(result1-result2).max() < tol
    
test_oper1()
test_oper2()
test_oper3()
test_oper4()
test_oper5()