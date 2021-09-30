# -*- coding: utf-8 -*-
"""
Created on Sun Aug 29 20:03:16 2021

@author: rodin
"""

import urllib.request as urllibr
import numpy as np
import matplotlib.gridspec as gridspec
import matplotlib.pyplot as plt


def load_dat():
    
    urllibr.urlretrieve('https://raw.githubusercontent.com/hplgit/scipro-primer/master/src/dictstring/viscosity_of_gases.dat',filename='c:/users/rodin/Documents/Python_Scripts/viscosity_of_gases.dat')
    inline=open('viscosity_of_gases.dat','r')
    
    mu_data={}
    C='C'
    T_0='T_0'
    mu_0='mu_0'
    line=inline.readline()
    
    while bool(line):

        if not(line.startswith('#')) and not(line.isspace()):
            tempvar=line.split()
            key_value=tempvar[0] if len(tempvar)==4 else ' '.join(tempvar[0:2])
            mu_data[key_value]={}
            mu_data[key_value][C]=eval(tempvar[1]) if len(tempvar)==4 else eval(tempvar[-3])
            mu_data[key_value][T_0]=eval(tempvar[2]) if len(tempvar)==4 else eval(tempvar[-2]) 
            mu_data[key_value][mu_0]=eval(tempvar[3]) if len(tempvar)==4 else eval(tempvar[-1]) 
        
        line=inline.readline()
    
    return mu_data

def mu(T,gas,mu_data):
    
    
    outputArg1=mu_data[gas]['mu_0']*((mu_data[gas]['T_0']-mu_data[gas]['C'])/(T+mu_data[gas]['C']))*(T/mu_data[gas]['T_0'])**1.5
    
    return outputArg1

def graph(mu_data):
    
    gases=['air','hydrogen','carbon dioxide']
    
    T=np.linspace(223,373,200)
    y_mat=np.zeros((len(gases),len(T)))
    
    plt.figure()
    gs=gridspec.GridSpec(1,3,wspace=0.9)
    for k in range(len(gases)):
        y_mat[k,:]=mu(T,gases[k],mu_data)
        
        plt.subplot(gs[k])
        plt.plot(T,y_mat[k,:])
        plt.xlabel('Temperature (K)')
        plt.ylabel('Viscosity')
        plt.title('Viscosity vs Temperature curve',fontdict={'fontsize': 7})
    
    plt.show()
    
mu_data=load_dat()

graph(mu_data)
        
    
    
        
        
    
    
    
        