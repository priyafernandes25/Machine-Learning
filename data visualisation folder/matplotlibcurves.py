# -*- coding: utf-8 -*-
"""
Created on Sat Mar 16 18:43:38 2019

@author: priya
"""
import matplotlib.pyplot as plt
import numpy as np

#Generate 20 points between 0 and 10 
x=np.linspace(0,5,5)


fig=plt.figure()
#first(1) n second(2) are x,y coordinates of the topleft corner,3(0.7) is width and 4(0.9) is height
a=fig.add_axes([0.1,0.2,0.7,0.8])

a.plot(x,x**2,'red',label="Square plot")
a.plot(x,x**3,'blue', label="Cube plot")
plt.show