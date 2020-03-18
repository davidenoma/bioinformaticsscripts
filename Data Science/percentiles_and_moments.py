# -*- coding: utf-8 -*-
"""
Created on Sat Jan 11 00:46:09 2020

@author: kora
"""

import numpy as np 
import matplotlib.pyplot as plt

vals = np.random.normal(10,1,10000)

plt.hist(vals,50)
plt.show()
#the 99th percential
np.percentile(vals,99)
np.percentile(vals,90)


#moment
#first moment is the mean 
np.mean(vals)
#second moment is the SD
np.std(vals)
#the thirs moment is skew
import scipy.stats as sp 
sp.skew(vals)

#The fourth moment is kurtosis 
sp.kurtosis(vals)
np.max(vals)