# -*- coding: utf-8 -*-
"""
Created on Wed Jun 30 21:02:37 2021

@author: rodin
"""

def sorttuple(inputArg1, inputArg2):
    
    tempvar=None
    for i in range(len(inputArg1)):
        for j in range(i+1,len(inputArg1)):
            if inputArg1[i][inputArg2-1] > inputArg1[j][inputArg2-1]:
                tempvar = inputArg1[i]
                inputArg1[i] = inputArg1[j]
                inputArg1[j] = tempvar

    return inputArg1

def printtuple(inputArg1):
    print()
    for i in inputArg1:
        print(i)
  
data = [ ('Alpha Centauri A', 4.3 , 0.26, 1.56), ('Alpha Centauri B', 4.3, 0.077, 0.45), ('Alpha Centauri C', 4.2, 0.00001, 0.00006), ("Barnard’s Star", 6.0, 0.00004, 0.0005), ('Wolf 359', 7.7, 0.000001, 0.00002), ('BD +36 degrees 2147', 8.2, 0.0003, 0.006), ('Luyten 726-8 A', 8.4, 0.000003, 0.00006), ('Luyten 726-8 B', 8.4, 0.000002, 0.00004), ('Sirius A', 8.6, 1.00, 23.6), ('Sirius B', 8.6, 0.001, 0.003), ('Ross 154', 9.4, 0.00002, 0.0005), ]
data=sorted(data,key=lambda obj: obj[2])        
printtuple(data)

data = [ ('Alpha Centauri A', 4.3 , 0.26, 1.56), ('Alpha Centauri B', 4.3, 0.077, 0.45), ('Alpha Centauri C', 4.2, 0.00001, 0.00006), ("Barnard’s Star", 6.0, 0.00004, 0.0005), ('Wolf 359', 7.7, 0.000001, 0.00002), ('BD +36 degrees 2147', 8.2, 0.0003, 0.006), ('Luyten 726-8 A', 8.4, 0.000003, 0.00006), ('Luyten 726-8 B', 8.4, 0.000002, 0.00004), ('Sirius A', 8.6, 1.00, 23.6), ('Sirius B', 8.6, 0.001, 0.003), ('Ross 154', 9.4, 0.00002, 0.0005), ]
data=sorttuple(data,3)
printtuple(data)



