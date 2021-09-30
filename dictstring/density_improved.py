# -*- coding: utf-8 -*-
"""
Created on Wed Aug 25 01:39:58 2021

@author: rodin
"""
import os
import pprint

def read_densities_v1():
    
    os.chdir('C:/users/rodin/Documents/Python_Scripts')
    f_ID=open('densities.dat','r')
    
    densities={}
    
    for line in f_ID:
        tempvar=line.split()
        densities[' '.join(tempvar[0:-1])]=float(tempvar[-1])
    
    f_ID.close()
    
    return densities

def read_densities_v2():
    
    inline=open('densities.dat','r')
    
    densities={}
    
    for line in inline:
        line=line.strip()
        densities[line[:12].rstrip()]=float(line[12:])
    
    inline.close()
    
    return densities

def test_read_densities():
    
    expect={'Earth core': 13.0,
 'Earth mean': 5.52,
 'Moon': 3.3,
 'Sun core': 160.0,
 'Sun mean': 1.4,
 'air': 0.0012,
 'gasoline': 0.67,
 'gold': 18.9,
 'granite': 2.7,
 'human body': 1.03,
 'ice': 0.9,
 'iron': 7.8,
 'limestone': 2.6,
 'mercury': 13.6,
 'platinium': 21.4,
 'proton': 230000000000000.0,
 'pure water': 1.0,
 'seawater': 1.025,
 'silver': 10.5}
    
    densities1 = read_densities_v1()
    densities2 = read_densities_v2()
    
    assert expect==densities1
    assert expect==densities2
    

test_read_densities()

densities1=read_densities_v1()
print()
pprint.pprint(densities1)

densities2=read_densities_v2()
print()
pprint.pprint(densities2)


