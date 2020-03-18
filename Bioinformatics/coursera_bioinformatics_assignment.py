# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""


import sys 

chars = "ACGT"

#Neighbors are sequences of equal length that differ by a hamming distance specified. 
def neighbors(pattern, d):
    assert(d <= len(pattern))

    if d == 0:
        return [pattern]

    r2 = neighbors(pattern[1:], d-1)
    
    r = [c + r3 for r3 in r2 for c in chars if c != pattern[0]]

    if (d < len(pattern)):
        r2 = neighbors(pattern[1:], d)
        r += [pattern[0] + r3 for r3 in r2]
    return r    

def mostFreqKmer(seq,pattern):
    count = 0 
    i = 0    
    endPoint = len(seq) - len(pattern) - 1
    while i < endPoint:
        if(seq[i:len(pattern)+i] == pattern):            
#            print(seq[i:len(pattern)+i])
            count += 1
        i += 1
#    return count  
          
#    
#def approximateMatchCount(text,pattern,d):
#        count = 0                  
#print(indexMax())
    
#print(mostFreqKmer(seq,"CAT"))
#print((neighbors(chars,3)))
myN= (neighbors("ACGT",3))
len(myN)
#for strN in myN:
#    print(strN)
#
#sys.stdout = open('ans2.txt','w')
#for strN in myN:
#    print(strN)



