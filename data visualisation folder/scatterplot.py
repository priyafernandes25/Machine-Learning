# -*- coding: utf-8 -*-
"""
Created on Sat Mar 16 19:57:38 2019

@author: priya
"""

import matplotlib.pyplot as plt
import numpy as np

x=np.linspace(0,10,30) #30 is no of points
y=np.sin(x)
plt.plot(x,y,'o',color='red')