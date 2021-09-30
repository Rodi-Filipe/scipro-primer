# -*- coding: utf-8 -*-
"""
Created on Sun Jul 18 15:23:34 2021

@author: rodin
"""

import numpy as np

def write_table_to_file(f, xmin, xmax, nx, ymin, ymax, ny, width=10, decimals=None, filename='filename'):
    
    strvar=['\n'+' '*width]
    with open(filename,'w') as f_ID:
        x=np.linspace(xmin,xmax,nx+1)
        y=np.linspace(ymax,ymin,ny+1)
        for i in range(len(y)):
            tempvar='%'+'%d.%d' %(width,decimals) + 'g' if decimals!=None else '%'+'%d' %(width) +'g'
            f_ID.write(tempvar %(y[i]))
            for j in range(len(x)):
                tempvar='%'+'%s.%s' %(width,decimals) + 'g' if decimals!=None else '%'+'%s' %(width) +'g'
                f_ID.write(tempvar %(f(x[j],y[i])))
                if i==len(y)-1:
                    strvar.append(tempvar %(x[j]))
            f_ID.write('\n')
        f_ID.write(''.join(strvar))
        f_ID.close()

def test_write_table_to_file(): 
    filename = 'table.dat' 
    write_table_to_file(f=lambda x, y: x + 2*y, xmin=0, xmax=2, nx=4, ymin=-1, ymax=2, ny=3, width=5, decimals=None, filename=filename) 
    # Load text in file and compare with expected results 
    with open(filename, 'r') as infile: 
        computed = infile.read() 
    expected = """\
    2    4  4.5    5  5.5    6
    1    2  2.5    3  3.5    4
    0    0  0.5    1  1.5    2
   -1   -2 -1.5   -1 -0.5    0

         0  0.5    1  1.5    2""" 
    assert computed == expected


test_write_table_to_file()