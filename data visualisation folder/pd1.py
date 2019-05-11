# -*- coding: utf-8 -*-
"""
Created on Sat Mar 16 19:46:23 2019

@author: priya
"""

import matplotlib.pyplot as plt
import pandas as pd

a=pd.read_excel(/*path* if \ doesnt work put \\ */,header=0)#header indicates the row number frm where the data needs to be displayed
print(a.head())#to check if correct data is extracted ..prints first 5 rows
x=a[['Date']]
datatoplot=a[['daily total female births in california 1959']]#column names
plt.plot(x,datatoplot)