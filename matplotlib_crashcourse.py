# -*- coding: utf-8 -*-
"""
Created on Sat Jan 11 16:22:15 2020

@author: kora
"""

import matplotlib.pyplot as plt
import numpy as np
from scipy.stats import norm
a = norm.pdf([1,2,3,4,5])
x = np.arange(-3,3,0.001)


plt.plot(x,norm.pdf(x))
plt.plot(x,norm.pdf(x,1.0,0.5))
plt.show()
#Making changes to the axes.

axes = plt.axes()
axes.set_xlim([-5,5])
axes.set_ylim([0,1.0])
axes.set_xticks([-5,-4,-3,-2,-1,0,1,2,3,4,5])
axes.set_yticks([0,0.1,0.2,0.3,0.4,0.5,0.6,0.7,0.8,0.9,1.0])
axes.grid()
plt.xlabel('Greebles')
plt.ylabel('probability');
plt.plot(x,norm.pdf(x),'b-')
plt.plot(x,norm.pdf(x,1.0,0.5),'r--')
plt.legend([' ','Gacks'],loc=4)
plt.show()


#Pie Chart
plt.rcdefaults()

values = [12,55,4,32,14]
colors = ['r','g', 'b', 'c', 'm']
explode = [0,0,0.2,0,0]
labels =['indi', 'nigeria', 'usa', 'belgium', 'taiwan']
plt.pie(values,colors=colors,labels=labels,explode =explode)
plt.title('Student Locations')
plt.show()

#Bar Chart 
values = [12,55,4,32,14]
colors=['r','g','b','c','m']
plt.bar(range(0,5), values, color=colors)
plt.show()
#Scatter plot  
X = [1,2,3,4,5,6]
Y=[100,150,105,189,124,11]
plt.rcdefaults()
plt.scatter(X,Y)
plt.show()
#Histogram
incomes = np.random.normal(2700,2,1000)
plt.hist(incomes,50)
plt.show()
#Box and Whisker Plot
uniformSkewed = np.random.rand(100) * 100 - 40 
high_outliers = np.random.rand(10) * 50 + 100
low_outliers = np.random.rand(10) * -50 - 100
data = np.concatenate((uniformSkewed,high_outliers,low_outliers))
plt.boxplot(data)
plt.show()

#Assignment 
ages = np.random.randint(80,size=100)
timeOnTv = np.random.randint(24,size=100)
plt.rcdefaults()
plt.xlabel="Ages"
plt.ylabel="Time on Tv"
plt.scatter(ages,timeOnTv)
plt.show


