import matplotlib.pyplot as plt
import matplotlib.animation as animation
from matplotlib.animation import FuncAnimation
from matplotlib.scale import LinearScale
import math
from math import sin, cos, radians
import time
from random import randint as rand
import numpy as np
from p5 import setup, draw, size, background, run

class point:
    def __init__(self,x,y):
        self.x=x 
        self.y=y 
    def __add__(self, p):
        return point(self.x+p.x,self.y+p.y)
    def __sub__(self, p):
        return point(self.x-p.x,self.y-p.y)
    def __mul__(self,s):
        return point(self.x*s,self.y*s)
    def print(self):
        print("(",self.x,",",self.y,")")


#utility functions
def GetOrthUnitVector(V):#V is a point
    if V.y==0:
        return point(0,1)
    v1=5
    v2=(-(V.x)/V.y)*v1
    magnitude=math.sqrt(v1**2+v2**2)
    v2=v2/magnitude
    v1=v1/magnitude
    return point(v1,v2)

def PrintPoints(points):
    for x in points:
        x.print()

def DrawRectangle(p):
    x, y = [p[i].x for i in range(4)], [p[i].y for i in range(4)]
    x.append(p[0].x)
    y.append(p[0].y)
    plt.plot(x,y)


class vehicle:
    def __init__(self, length, width, speed_limit, acc_limit, centroid, angle, v, a):
        #parameters
        self.length = length
        self.width = width
        self.speed_limit = speed_limit 
        self.acc_limit = acc_limit 
        #state variables
        self.centroid = centroid 
        self.angle = angle 
        self.v = v
        self.a = a
    def StateToCorners(self):
        dir_vect=point(math.cos(self.angle),math.sin(self.angle))
        dir_vect=dir_vect*(self.length/2)
        orth_vect=GetOrthUnitVector(dir_vect)
        orth_vect=point(orth_vect.x*(self.width)/2,orth_vect.y*(self.width)/2)
        points=[]
        points.append(self.centroid+dir_vect+orth_vect)
        points.append(self.centroid+dir_vect-orth_vect)
        points.append(self.centroid-dir_vect-orth_vect)
        points.append(self.centroid-dir_vect+orth_vect)
        return points
    def DrawVehicle(self):
        p=self.StateToCorners()
        DrawRectangle(p)
        
        plt.plot(self.centroid.x,self.centroid.y,marker="o",markersize=5,markerfacecolor="green")
        ax = plt.gca()
        ax.set_aspect('equal', adjustable='box')
        plt.show()
    def ShortestDistance(self,V):
        veh1=self.StateToCorners()
        veh2=V.StateToCorners()
        min=99999999
        for i in veh1:
            for j in veh2:
                dist = math.dist([i.x, i.y], [j.x, j.y])
                if dist<min:
                    min=dist
        return min
    def controller(self):
        return self.a #will return acceleration at t+1 using acceleration at t
    def updateStateVars(self):
            self.v=self.v+(self.controller()*dt)
            self.centroid=self.centroid+self.v*dt
            self.angle=math.atan2(self.v.y,self.v.x)
    def getxyLists(self):
        p=self.StateToCorners()
        x, y = [p[i].x for i in range(4)], [p[i].y for i in range(4)]
        x.append(p[0].x)
        y.append(p[0].y)
        return x,y
    