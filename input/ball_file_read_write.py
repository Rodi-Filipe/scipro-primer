# -*- coding: utf-8 -*-
"""
Created on Tue Jul  6 18:18:40 2021

@author: rodin
"""

def get_input(str):
    
    filename=''.join(['C:/Users/rodin/OneDrive/Documents/',str])
    f_ID=open(filename,'r')
    outputArg1=eval(f_ID.readline().split()[-1])
    
    f_ID.readline()
    outputArg2=[]
    while True:
        tempvar=f_ID.readline()
        if bool(tempvar):
            tempvar2=tempvar.split()
            [outputArg2.append(eval(i)) for i in tempvar2]  
        else:
            break
    f_ID.close()
    return outputArg1,outputArg2

def get_input1(str):
    filename=''.join(['C:/Users/rodin/OneDrive/Documents/',str])
    f_ID=open(filename,'r')
    outputArg1=eval(f_ID.readline().split()[-1])
    
    f_ID.readline()
    tempvar=f_ID.readline()
    outputArg2=[]
    while bool(tempvar):
        tempvar2=tempvar.split()
        [outputArg2.append(eval(i)) for i in tempvar2]  
        tempvar=f_ID.readline()
    f_ID.close()
    return outputArg1,outputArg2

def print_input(vo,t):
    t=sorted(t)
    g=9.81
    y=[ vo*i-0.5*g*i**2 for i in t]
    print('   t          y')
    [print('%6.3f %9.3f' %(t[i], y[i])) for i in range(len(t))]
    
def test_file():
    
    f_ID=open('C:/Users/rodin/OneDrive/Documents/ball2.txt','w')
    f_ID.write("""v0: 4.78
t:
0.15592  0.28075   0.36807889 0.35 0.57681501876
0.21342619  0.0519085  0.042  0.27  0.50620017 0.528
0.2094294  0.1117  0.53012  0.3729850  0.39325246
0.21385894  0.3464815 0.57982969 0.10262264
0.29584013  0.17383923""")
    f_ID.close()
    
    vo, t=get_input('ball2.txt')
    
    msg='Test failed'
    assert isinstance(vo,float), msg
    assert isinstance(t,list), msg

test_file()
vo, t = get_input1('ball.txt')
op=print_input(vo,t)
