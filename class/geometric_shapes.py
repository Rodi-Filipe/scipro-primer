# -*- coding: utf-8 -*-
"""
Created on Sat Sep 18 20:41:03 2021

@author: rodin
"""
from math import sqrt

class rectangle(object):
    
    def __init__(self,w,h,point):
        
        self.w=w
        self.h=h
        self.point=point
    
    @property
    def point(self):
        return self._point
    
    @point.setter
    def point(self,value):
        if isinstance(value,(tuple,list)):
            self._point=value
        else:
            raise TypeError('Invalid type for point property')
   
    def area(self):
        
        return self.w*self.h
    
    def perimeter(self):
        
        return 2*self.w+2*self.h
    
class triangle(object):
    
    def __init__(self,point1,point2,point3):
        
        self.point1=point1
        self.point2=point2
        self.point3=point3
    
    def area(self):
        
        return 0.5*abs(self.point2[0]*self.point3[1]-self.point3[0]*self.point2[1]-self.point1[0]*self.point3[1]+self.point3[0]*self.point1[1]\
            +self.point1[0]*self.point2[1]-self.point2[0]*self.point1[1])
    
    def perimeter(self):
        
        d_ab=sqrt((self.point1[0]-self.point2[0])**2+(self.point1[1]-self.point2[1])**2)
        d_bc=sqrt((self.point2[0]-self.point3[0])**2+(self.point2[1]-self.point3[1])**2)
        d_ad=sqrt((self.point1[0]-self.point3[0])**2+(self.point1[1]-self.point3[1])**2)
        
        return d_ab+d_bc+d_ad

def test_triangle():
    
    point1=(1,2)
    point2=(4,5)
    point3=(4,0)

    tr1=triangle(point1,point2,point3)    
    expct1=7.5000000
    expct2=12.848192
    
    assert abs(tr1.area()-expct1) < 1E-4, '%6.4f != to %6.4f' %(tr1.area(),expct1)
    assert abs(tr1.perimeter()-expct2) < 1E-5, '%4.3f != to %4.3f' %(tr1.perimeter(),expct2)
    
    
def test_rectangle():

    w=6
    h=10
    point=(0,0)
    
    rct1=rectangle(w,h,point)
    expct1=6*10
    expct2=2*6+2*10
    
    assert abs(rct1.area()-expct1) < 1E-5, '%4.3f != to %4.3f' %(rct1.area(),expct1)
    assert abs(rct1.perimeter()-expct2) < 1E-5, '%4.3f != to %4.3f' %(rct1.perimeter(),expct2)
    
if __name__ == '__main__':
    
    test_triangle()
    test_rectangle()
    

         
        