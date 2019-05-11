# -*- coding: utf-8 -*-
"""
Created on Sat Mar 16 18:35:08 2019

@author: priya
"""
import numpy as np
a=np.array([[1,4,2],[3,4,6],[0,-1,5]])

#Sorted Array 
print("Array elements in sorted order:\n",np.sort(a,axis=None))

#Sorted Array row-wise
print("Row-wise sorted array:\n",np.sort(a,axis=1))

#Sorted Array column-wise
print("Column-wise sorted array:\n",np.sort(a,axis=0))

#Specify sorting technique
print("Column-wise sorted array by applying merge-sort:\n",np.sort(a,axis=0,kind='mergesort'))