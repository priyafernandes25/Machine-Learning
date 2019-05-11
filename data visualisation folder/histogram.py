# -*- coding: utf-8 -*-
"""
Created on Sat Mar 16 19:31:40 2019

@author: priya
"""

import matplotlib.pyplot as plt
import numpy as np

x=np.random.random_integers(1,100,10)
#bins are used to grp data and increase spacing(readability) Avg take 50
plt.hist(x, bins=30)
plt.ylabel('No of times')
plt.title("Plotting Random numbers")
plt.show()#not required