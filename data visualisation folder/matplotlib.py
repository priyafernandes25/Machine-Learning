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

plt.title("MY FIRST PLOT")
plt.xlabel("X-axis")
plt.ylabel("Y-axis")
plt.plot(x,y)
plt.show