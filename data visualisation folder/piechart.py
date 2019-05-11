# -*- coding: utf-8 -*-
"""
Created on Sat Mar 16 20:16:03 2019

@author: priya
"""

import matplotlib.pyplot as plt
import numpy as np

#The slice names of a population distribution pie chart
pieLabels='Asia','Africa','Europe','North America','south America','Australia'

#Population data
populationShare=[59.69,16,9.94,7.79,5.68,0.54]
#abv list r always in percentages
figureObject, axesObject=plt.subplots()
#figureObject is a contaainer...it cantains axis obj
#axesObjects gives diff axes(Asia,africa , etc..)

#Draw the pie chart
axesObject.pie(populationShare,labels=pieLabels,autopct='%1.2f',startangle=180)
#change startangle to avoid overlapping of namees

#Aspect ratio-equal means pie in a circle
axesObject.axis('equal')
