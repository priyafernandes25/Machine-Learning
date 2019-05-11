# -*- coding: utf-8 -*-
"""
Created on Sat Mar 16 20:07:31 2019

@author: priya
"""

import matplotlib.pyplot as plt
import numpy as np

rng=np.random.RandomState(0)#generates diff values can be int , 2 dec values or 5 dec values
x=rng.randn(100)
y=rng.randn(100)
colors=rng.rand(100)
sizes=1000*rng.rand(100)
plt.scatter(x,y,c=colors,s=sizes,alpha=0.3,cmap='viridis')#viridis is a type of color map, you can use 'Gray' too
plt.colorbar()
#if data is overlapping then use small alpha