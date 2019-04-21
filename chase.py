# -*- coding: utf-8 -*-
"""
Created on Tue Apr 16 00:16:03 2019

@author: sreeh

import turtle

#window=turtle.Screen()

t=turtle.Turtle()

t.dot()

t.forward(29)

turtle.backward(60)


turtle.done()


"""

import time
import bokeh
import random 
import math
import matplotlib
import turtle
from matplotlib import pyplot as plt
from numpy import zeros
import numpy  as np
import random

from tqdm import tqdm
import matplotlib.animation as animation
from matplotlib import style


t=[0,1000]
m=[500,0]
mx=[500]
my=[0]
#d=[0,0]
dlt=14

flipx=1
flipy=1

def move_target(flipx,flipy):


    if(t[0]<10):
        flipx=1
    if(t[0]>990):
        flipx=-1
        
    if(t[1]<10):
        flipy=1
    if(t[1]>990):
        flipy=-1
    
        
        
        
    x = random.uniform(0,9)
    if(x<7.5):
        t[0]+=dlt*flipx
    else:
        t[0]-=dlt*flipx
        
    y = random.uniform(0,9)
    
    if(y<6.5):
        t[1]+=dlt*flipy
    else:
        t[1]-=dlt*flipy
    
    return t,flipx,flipy

def distance(t,m):
    x=t[0]-m[0]
    y=t[1]-m[1]
    dist=math.sqrt((x*x)+(y*y))
    
    return dist,x,y
    

def speed(dist):
    speed=dist/100
    return speed

def pos(d):
    if(d>50):
        return 1
    elif(d>0):
        return (d/50)
    else:
        return 0
    
def neg(d):
    if(d<-50):
        return 1
    elif(d>-50 and d<0):
        return (d/-50)
    else:
        return 0

def zero(d):
    return 0
    
def miss_x(x,dist):
    
    mn=neg(x)
    mp=pos(x)
    mz=zero(x)

    
      
    dire_x=(mp)+(-1*mn)+mz
    
    return dire_x

def miss_y(y,dist):
    
    
    mn=neg(y)
    mp=pos(y)
    mz=zero(y)
        
    dire_y=(mp)+(-1*mn)+mz
    
    return dire_y

def move_miss(t,m):
    
    print(m)
    
    
    dist,x,y=distance(t,m)
    
    vel=speed(dist)+12
    dire_x=miss_x(x,dist)
    dire_y=miss_y(y,dist)
    
    
    m[0]+=vel*dire_x
    m[1]+=vel*dire_y
    
    mx.append(m[0])
    my.append(m[1])
    
        
            
    return dist,mx,my  


"""

def draw(t,mx,my):

    fig.clear()

    plt.scatter(t[0],t[1],marker='^')
    plt.plot(mx,my,color='r')
    plt.xlim(0,1000)
    plt.ylim(0,1000)
    plt.pause(0.2)
    plt.show


def animate(i):
    ax1.plot(mx,my)
    ax1.scatter(t[0],t[1])
    
#turtle scenece 
"""


dist,x,y=distance(t,m)



fig=plt.figure()

while(dist>10):
    fig.clear()
    
    dist,mx,my=move_miss(t,m)
    plt.scatter(t[0],t[1],marker='^')
    plt.plot(mx,my,color='r')
    plt.xlim(0,1000)
    plt.ylim(0,1000)

    #ani=animation.FuncAnimation(fig,animate,interval=10)
    
    plt.pause(0.05)
    plt.show

    
    
    t,flipx,flipy=move_target(flipx,flipy)
    

print("target is down")
    





























        
