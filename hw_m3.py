# -*- coding: utf-8 -*-
"""
Created on Wed Nov 20 18:38:51 2019

@author: rost_
"""
from mpl_toolkits.mplot3d import Axes3D
import matplotlib.pyplot as plt
import numpy as np


"""
1. Задание
Даны два вектора в трехмерном пространстве: (10,10,10) и (0,0,-10)

Напишите код на Python, реализующий расчет длины вектора, заданного его координатами. (в программе)
"""


a=[10, 10, 10]
b=[0, 0, -10]
sum_ab0=[]
for i in range(len(a)):
    sum_ab0.append(a[i]+b[i])
print('Summ vector: ',sum_ab0)
    
a=np.array(a)
b=np.array(b)
sum_ab1 = a+b
print('Summ vector: ',sum_ab1)

len_ab=0.
for i in range(len(sum_ab0)):
    len_ab=len_ab+sum_ab0[i]**2
len_ab=np.sqrt(len_ab)    
print('Summ vector len : ', len_ab)
print('Summ vector len : ', np.linalg.norm(sum_ab0))

#==============================================================================
"""
3. Задание (в программе)
Напишите код на Python, реализующий построение графиков:
окружности,
эллипса,
гиперболы.

"""


fig = plt.figure('cycle')
ax = plt.gca()
ax.spines['left'].set_position('center')
ax.spines['bottom'].set_position('center')
ax.spines['top'].set_visible(False)
ax.spines['right'].set_visible(False)


R=10
x = np.linspace(-10,10, 300)
y1 = np.sqrt(R**2*(1-x**2/R**2))
y2 = -np.sqrt(R**2*(1-x**2/R**2))

plt.axis('equal')                        

plt.plot(x, y1)
plt.plot(x, y2)




fig = plt.figure('ellipse')
ax = plt.gca()
ax.spines['left'].set_position('center')
ax.spines['bottom'].set_position('center')
ax.spines['top'].set_visible(False)
ax.spines['right'].set_visible(False)


R1=10
R2=20

x = np.linspace(-20,20, 300)
y1 = np.sqrt(R1**2*(1-x**2/R2**2))
y2 = -np.sqrt(R1**2*(1-x**2/R2**2))

plt.axis('equal')                        

plt.plot(x, y1)
plt.plot(x, y2)



fig = plt.figure('hyperbola')
ax = plt.gca()
ax.spines['left'].set_position('center')
ax.spines['bottom'].set_position('center')
ax.spines['top'].set_visible(False)
ax.spines['right'].set_visible(False)


R1=10
R2=20

x = np.linspace(-200,200, 300)
y1 = np.sqrt(R1**2*(1+x**2/R2**2))
y2 = -np.sqrt(R1**2*(1+x**2/R2**2))

plt.axis('equal')                        

plt.plot(x, y1)
plt.plot(x, y2)
















X = np.arange(-5, 5, 0.15)
Y = np.arange(-5, 5, 0.15)
X, Y = np.meshgrid(X, Y)



Z =2*X+3*Y

fig = plt.figure()
ax = Axes3D(fig)
ax = fig.gca(projection='3d')
ax.plot_surface(X, Y, Z)
ax.scatter(0,0,0,'z',50,'red')



Z =2*X+3*Y+5
ax.plot_surface(X, Y, Z)

plt.show()





def plot():
    fig = plt.figure()
    ax = Axes3D(fig)
    ax = fig.gca(projection='3d')
    ax.plot_surface(X, Y, Z)
#    ax.plot_wireframe(X, Y, Z)
    
    ax.scatter(0,0,0,'z',50,'red')
    ax.plot_surface(X, Y, -Z)
#    ax.plot_wireframe(X, Y, -Z)
    
    
    plt.show()
    

Z =1*np.sqrt(1-(X/3)**2 - 1*(Y/3)**2)
plot()
Z =1*np.sqrt(1-(X/3)**2 + 1*(Y/3)**2)
plot()
Z =1*np.sqrt(1+(X/3)**2 + 1*(Y/3)**2)
plot()
Z =1*np.sqrt(1+(1/X)**2 + 1*(1/Y)**2)
plot()

Z =(X)**2 - 3*(Y)**2
plot()


