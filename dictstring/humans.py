# -*- coding: utf-8 -*-
"""
Created on Sun Aug 29 03:53:36 2021

@author: rodin
"""

import urllib.request as urllibr
from pprint import pprint
import pandas

def loaddat():
    
    urllibr.urlretrieve('https://raw.githubusercontent.com/hplgit/scipro-primer/master/src/dictstring/human_evolution.txt',filename='c:/users/rodin/Documents/Python_Scripts/human_evolution.txt')
    inline=open('human_evolution.txt','r')
    
    data={}
    line=inline.readline()
    
    while bool(line):
        if 'Species' in line:
            indx1=line.find('Lived')
            indx4=line.find('Brain volume')
        elif '(mill. yrs)' in line:
            indx2=line.find('height')
            indx3=line.find('mass')
        elif 'H.' in line:
            key=''.join(line[0:indx1]).strip()
            data[key] = {}
            data[key]['when'] = (line[indx1:indx2]).strip()
            data[key]['height']=(line[indx2:indx3]).strip()
            data[key]['mass']=(line[indx3:indx4]).strip()
            data[key]['Brain volume']=(line[indx4:]).strip()
        
        line=inline.readline()
    
    return data

def format_data(data):
        
    string='Species               Lived when      Adult        Adult       Brain volume'
    n=len(string)
    
    indx1=string.find('Lived')
    indx4=string.find('Brain volume')
    print(string)
    
    string='                      (mill. yrs)     height (m)   mass (kg)   (cm**3) '
    indx2=string.find('height')
    indx3=string.find('mass')
    print(string)
    
    print('-'*(n+4))
    
    for key in data:
        print(key,end=' '*(indx1-len(key)))
        count=1
        for column_name in data[key]:
            if count==2:
                print(data[key][column_name],end=' '*((indx3-indx2)-len(data[key][column_name])))
            elif count==3:
                print(data[key][column_name],end=' '*((indx4-indx3)-len(data[key][column_name])))
            elif count==4:
                print(data[key][column_name])
            else:
                print(data[key][column_name],end=' '*((indx2-indx1)-len(data[key][column_name])))
             
            count+=1
    
    print('-'*(n+4))            
            
data = loaddat()

format_data(data)
