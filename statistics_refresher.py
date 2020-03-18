# -*- coding: utf-8 -*-
"""
Created on Fri Jan 10 16:08:14 2020

@author: kora
"""

import numpy as np

incomes = np.random.normal(27000,15000,10000)
np.mean(incomes)

#segmenting the data 

import matplotlib.pyplot as plt
plt.hist(incomes, 50)
plt.show

ages = np.random.randint(10,high=90, size=200)
 
from scipy import stats 
stats.mode(ages)

##Standard deviation and variance    
incomes = np.random.normal(100.0, 20.0,1000)
plt.hist(incomes,50)
plt.show()
 
##Data distributions 
values = np.random.uniform(-10.0,10,10000)
plt.hist(values,50)
plt.show()

#Visualize the probability density function
from scipy.stats import norm 
x = np.arange(-3,3,0.1)
plt.plot(x,norm.pdf(x))

#Exponential pdf 
from scipy.stats import expon
x = np.arange(0,10,0.001)
plt.plot(x,expon.pdf(x))
plt.show()

#Binomial probability mass function 
from scipy.stats import binom
n,p = 10, 0.5
x = np.arange(0,10,0.001)
plt.plot(x, binom.pmf(x, n, p ));
xBinom = binom.pmf(x,n,p)
##Poisson pmf
from scipy.stats import poisson 
mu = 500
x = np.arange(400,600,0.5)
plt.plot(x,poisson.pmf(x,mu))


