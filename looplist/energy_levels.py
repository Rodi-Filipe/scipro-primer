# -*- coding: utf-8 -*-
"""
Created on Fri Jun 18 23:09:48 2021

@author: rodin
"""

m_e=9.1094*10**-31
e=1.6022*10**-19
epsilon_o=8.8542*10**-12
h=6.6261*10**-34
c=-(m_e*(e)**4)/(8*(epsilon_o**2)*(h**2))

n=20
E_n=[0]*n

print('\n')
for i in range(1,n+1):
    E_n[i-1]=c*(1/i**2)
    print('%5.2g'%(E_n[i-1]))
    
print()

delta_E=[[0]*5, [0]*5, [0]*5, [0]*5, [0]*5]

for i in range(1,6):
    for j in range(1,6):
        delta_E[j-1][i-1]=(c*(1/i**2-1/j**2))

for i in range(0,5):
    for j in range(0,5):
        myvar=delta_E[j][i]
        print('%7.1g' % myvar, end=' ')
    print()
    
    
    
        
    
    
    
    
