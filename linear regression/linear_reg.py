# -*- coding: utf-8 -*-
"""
Created on Sat Mar 23 19:28:47 2019

@author: priya
"""

import pandas as pd
import matplotlib.pyplot as plt
from sklearn.linear_model import LinearRegression
import statsmodels.api as sm

data=pd.read_excel("C:\\Users\\priya\\Documents\\Python Scripts\\linear regression\\webratings.xlsx")
data.head()
print(data.head())
plt.figure(figsize=(12,6))
plt.scatter(data['User'],data['ratings'],c='blue')
plt.xlabel("Users_")
plt.ylabel("Ratings out of 5")
#plt.show()

#now creating linear approximation
x=data['User'].values.reshape(-1,1)
y=data['ratings'].values.reshape(-1,1)
reg=LinearRegression()
reg.fit(x,y)

#reg.coef_[0][0] calculates slope, reg.intercept_ calculates 'c'
print("The linear model is: Y = {:.5}X + {:.5}".format(reg.coef_[0][0],reg.intercept_[0]))

#now creating prediction
predictions=reg.predict(x)
plt.figure(figsize=(12,6))
plt.scatter(data['User'],data['ratings'],c='black')
plt.scatter(data['User'],predictions,c='red',linewidth=1)
plt.xlabel("Users_")
plt.ylabel("Ratings_")

#now accessing efficiency using R-squared model
x=data['User']
y=data['ratings']
x2=sm.add_constant(x)
#Ordinary Least Squares is the simplest and most common estimator in which the two \(\beta\)s are chosen to minimise the square of the distance between
est=sm.OLS(y,x2)
est2=est.fit()
#print(est2.summary())

print("Enter user number: ")
p=int(input())
rate=p*reg.coef_[0][0]+reg.intercept_[0]
print("User will rate: ",rate)