# -*- coding: utf-8 -*-
"""
Created on Tue Jan 14 17:39:03 2020

@author: kora
"""

import numpy
numpy.__version__


range(10)
x = range(10)
x
type(x)
list(x)

z = [str(a) for a in y]

type(z)
c = [True, 1, 'tree', 4.0]
[type(item) for item in c]
l = list(range(10))
import array

array.array('i',l)
d = array.array('i',l)
d
type(d)
import numpy as np

np.array([range(i,i+3) for i in [1,2,3]])
d = np.array([range(i,i+3) for i in [1,2,3]])
type(d)
np.zeros(10,dtype=float)


age = np.random.random((3,3))
age
type(age)
age *100
age
type(age)

np.random.normal(10,(2,2))
np.random.normal(10,1,(2,2))
np.random.normal(10,0.1,(2,2))
c = np.random.normal(10,0.1,(2,2))

np.random.randint

np.random.randint(0,10,(5,100))

np.random.randint(10,size=(3,3))
