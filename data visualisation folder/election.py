# -*- coding: utf-8 -*-
"""
Created on Sat Mar 16 20:37:37 2019

@author: priya
"""

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import collections

#merging two excel files
df=pd.DataFrame()
for f in['C:\\Users\\priya\\Documents\\electiondataset\\set1.xlsx','C:\\Users\\priya\\Documents\\electiondataset\\set2.xlsx']:
    data=pd.read_excel(f,'Sheet1') #this loop merges the two excel sheets into one.
    df=df.append(data)
    
df.to_excel('C:\\Users\\priya\\Documents\\electiondataset\\combined.xlsx')#resultant data
data=pd.read_excel('C:\\Users\\priya\\Documents\\electiondataset\\combined.xlsx')
print(data)