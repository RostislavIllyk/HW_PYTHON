# -*- coding: utf-8 -*-
"""
Created on Wed Nov 20 18:38:51 2019

@author: rost_
"""

import numpy as np
import matplotlib.pyplot as plt


x = np.linspace(-3,3, 300)
y = np.sin(x)
##plt.plot(x)
## псевод ось X
#plt.plot([-3,3],[0,0], color='g')
## псевод ось Y
#plt.plot([0,0], [-1.1,1.1], color='g')

ax = plt.gca()
ax.spines['left'].set_position('center')
ax.spines['bottom'].set_position('center')
ax.spines['top'].set_visible(False)
ax.spines['right'].set_visible(False)

x = np.linspace(-3,3, 300)

y = np.cos(x)
plt.plot(x, y)

y = np.cos(3*x)
plt.plot(x, y)
