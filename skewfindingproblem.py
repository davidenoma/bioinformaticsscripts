# -*- coding: utf-8 -*-
"""
Created on Wed Jan 15 15:56:38 2020

@author: kora
"""

def skew(seq):
    skew = [0]
    for i in range(1, len(seq)):       
        skew.append(skew[-1])     
        if seq[i - 1] == "G": 
            skew[i] = skew[i - 1] + 1
        elif seq[i - 1] == "C":
            skew[i] = skew[i - 1] - 1
    return skew
seq="CATGGGCATCGGCCATACGCC"

skewList = skew(seq)

maxSkewValue=max(skewList)
minSkewValue=min(skewList)

def indexMax():    
    skewMax = []
    index = 0
    for pos in skew(seq):
        
        if(pos == minSkewValue):
            skewMax.append(index)
        index += 1
    return skewMax   
print(indexMax())