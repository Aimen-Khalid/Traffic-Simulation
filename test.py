import matplotlib.pyplot as plt
import math

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

class vehicle:
    def __init__(self, length, width, speed_limit, acc_limit, centroid, angle):
        #parameters
        self.length = length
        self.width = width
        self.speed_limit = speed_limit 
        self.acc_limit = acc_limit 
        #state variables
        self.centroid = centroid 
        self.angle = angle 
    def StateToCorners(self):#takes vehicle object as input
        dir_vect=point(math.cos(self.angle),math.sin(self.angle))
        dir_vect=dir_vect*(self.length/2)
        orth_vect=GetOrthUnitVector(dir_vect)
        orth_vect=point(orth_vect.x*(self.width)/2,orth_vect.y*(self.width)/2)
        points=[]
        points.append(self.centroid+dir_vect+orth_vect)
        points.append(self.centroid+dir_vect-orth_vect)
        points.append(self.centroid-dir_vect-orth_vect)
        points.append(self.centroid-dir_vect+orth_vect)
        PrintPoints(points)
        return points
    def DrawVehicle(self):
        p=self.StateToCorners()
        plt.plot([p[0].x,p[1].x],[p[0].y,p[1].y])
        plt.plot([p[1].x,p[2].x],[p[1].y,p[2].y])
        plt.plot([p[2].x,p[3].x],[p[2].y,p[3].y])
        plt.plot([p[3].x,p[0].x],[p[3].y,p[0].y])
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

def main():
    l=6
    w=2
    angle=math.radians(60)
    centroid=point(-7,-6)
    V=vehicle(l,w,0,0,centroid,angle)
    V.DrawVehicle()


    l=6
    w=4
    angle=math.radians(205)
    centroid=point(8,6)
    V1=vehicle(l,w,0,0,centroid,angle)
    
    print(V.ShortestDistance(V1))

if __name__ == "__main__":
    main()