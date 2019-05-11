# -*- coding: utf-8 -*-
"""
Created on Sat Mar 16 18:43:38 2019

@author: priya
"""
import matplotlib.pyplot as plt
import numpy as np

#Generate 20 points between 0 and 10 
x=np.linspace(0,10,20)

#generate array 'y' from square of:
y=x**2

plt.subplot(2,2,1)
plt.plot(x,y,'red')

y=x
plt.subplot(2,2,2)
plt.plot(y,x,'green')

plt.subplot(2,2,3)
plt.plot(x,y,'blue')

plt.subplot(2,2,4)
plt.plot(x,y,'yellow')

