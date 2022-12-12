# -*- coding: utf-8 -*-
"""
Created on Tue Sep 14 00:39:41 2021

@author: rodin
"""

import os
import tarfile
import urllib.request as urllibr
import sys
import numpy as np
from scitools import pprint2
import matplotlib.pyplot as plt
import datetime as dt
import matplotlib.gridspec as gridspec
from matplotlib.dates import YearLocator, MonthLocator, DateFormatter


def get_file_mapping():

    os.chdir('c:/users/rodin/Documents/Python_Scripts')
    urllibr.urlretrieve('https://github.com/hplgit/scipro-primer/raw/master/src/misc/city_temp.tar.gz',filename='city_temp.tar.gz')

    with tarfile.open('city_temp.tar.gz','r:gz') as tempfile:
        def is_within_directory(directory, target):
            
            abs_directory = os.path.abspath(directory)
            abs_target = os.path.abspath(target)
        
            prefix = os.path.commonprefix([abs_directory, abs_target])
            
            return prefix == abs_directory
        
        def safe_extract(tar, path=".", members=None, *, numeric_owner=False):
        
            for member in tar.getmembers():
                member_path = os.path.join(path, member.name)
                if not is_within_directory(path, member_path):
                    raise Exception("Attempted Path Traversal in Tar File")
        
            tar.extractall(path, members, numeric_owner=numeric_owner) 
            
        
        safe_extract(tempfile)

    infile=open('citylistWorld.htm','r')

    line=infile.readline()
    mapping = {}
    
    while bool(line):
        if "     mso-list:l" in line:
            city=line.split("<b>")[1].replace(' ( </b>','').replace('</b>','') 
            tempvar=infile.readline()
            line = tempvar if '     href=' in tempvar else infile.readline()
            filename=line[(line.find('gsod/')+len('gsod/')):line.find('">')]
            mapping[city]=filename
        
        line=infile.readline()
    
    infile.close()
    
    return mapping

def read_dat(mapping,city):

    filename=mapping[city]
    if not(os.path.isfile(filename)):
        raise ValueError('Invalid city name')
        sys.exit(1)
    else:
        #infile=open(filename,'r')
        data=np.genfromtxt(fname=filename,dtype=str,missing_values='-99',filling_values=0)
        dates=[dt.datetime(int(y),int(m),int(d)) for m,d,y in data[:,0:-1].tolist()]
        
        temperatures=np.asarray(data[:,-1],dtype=float)
        data={}
        data['city']=city
        data['dates']=np.asarray(dates)
        data['temperature']=temperatures
        
    return data        

def plot_data(city_data_dict,period):
    
    
    datemin=dt.datetime(period[0],1,1)
    datemax=dt.datetime(period[1],1,1)
    
    fig=plt.figure()
    fig.set_size_inches(30,30)
    gs=gridspec.GridSpec(len(city_data_dict),1,hspace=1)
    ax=plt.gca()
    counter=0
    for city_data in city_data_dict:
        plt.subplot(gs[counter])
        plt.plot_date(city_data['dates'],city_data['temperature'],'_')
        plt.xlabel('dates')
        plt.ylabel('Temperature')
        plt.title('Temperature vs Dates for %s' % city_data['city'])
        plt.xlim((datemin,datemax))
        years = YearLocator() # major ticks every 5 years 
        months = MonthLocator(5) # minor ticks every 6 months 
        yearsfmt = DateFormatter('%Y') 
        ax.xaxis.set_major_locator(years) 
        ax.xaxis.set_major_formatter(yearsfmt) 
        ax.xaxis.set_minor_locator(months) 
        fig.autofmt_xdate()
        counter+=1
    
    plt.show()

pprint2.pprint(get_file_mapping())
Munich_data=read_dat(get_file_mapping(),'Munich')
Lisbon_data=read_dat(get_file_mapping(),'Lisbon')
London_data=read_dat(get_file_mapping(),'London')
Tokyo_data=read_dat(get_file_mapping(),'Tokyo')
plot_data([Munich_data,Lisbon_data,London_data,Tokyo_data],[2004,2008])
