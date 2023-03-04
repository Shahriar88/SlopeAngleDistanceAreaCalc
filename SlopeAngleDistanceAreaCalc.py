# -*- coding: utf-8 -*-
"""
Created on Sat Mar  4 03:48:59 
From cartesian coordinates: get slope, angle, distance between two points and area of a polygon.
@author: shahr
"""
from math import atan2,degrees,sqrt

def get_slope(pos1,pos2): # list
    m=(pos2[1]-pos1[1])/(pos2[0]-pos1[0])
    return m
#------------------------------------
def get_angle(pos1,pos2): # list
    r=atan2((pos2[1]-pos1[1]),(pos2[0]-pos1[0]))
    d=degrees(r)
    return r,d
#------------------------------------
def get_distance(pos1, pos2): # list
    x=abs(pos1[0]-pos2[0])
    y=abs(pos1[1]-pos2[1])
    return sqrt(x*x+y*y)
#------------------------------------
def get_area(list_): # list
    n=len(list_)
    t=list_[0]
    list_.append(t)
    result=0
    for i in range(n):
        x1=list_[i][0]
        y1=list_[i][1]
        x2=list_[i+1][0]
        y2=list_[i+1][1]
        result=result + x1*y2-x2*y1
    result=abs(result)/2
    return result
#------------------------------------
if __name__=='__main__':
    slope=get_slope([1,1],[5,5])
    rad, deg=get_angle([1,1],[5,5])
    rad2, deg2=get_angle([5,5],[1,1])
    
    distance=get_distance([5,5],[1,1])
    distance2=get_distance([5,5],[8,1])
    
    polygon=[[0,0],[2,3],[5,6],[10,10]]
    area=get_area(polygon)