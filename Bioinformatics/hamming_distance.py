# -*- coding: utf-8 -*-
"""
Created on Wed Jan 15 12:34:07 2020

@author: kora
"""

def hamming_distance(s1,s2):
#    Hamming is the total numper of positions
#    wherein the two nucleotide sequences differ.
    if len(s1) != len(s2):
        raise ValueError("Undefined for sequences of unequal length");
    return sum(ch1 != ch2 for ch1, ch2 in zip(s1,s2))
 

#[(x,y) for x in [1,2,3,4]]
def approximatePatternCount(text,pattern,d):
    count = 0 
    for i in range(len(text)-len(pattern)):
        approxPattern = text[i:i+len(pattern)]
        
        if(hamming_distance(pattern,approxPattern) <= d):
#            print(approxPattern)
            count +=1
    return count

    
def d(pattern, text):
##    This defines the minimum hamming distance between pattern and any k-mer in
##    the text
    hamming_distances = []
    ham_dist_patn = {}
    for i in range(len(text)-len(pattern)):
        
        hamming_distances.append(hamming_distance(pattern,text[i:i+len(pattern)]))
        # ham_dist_patn[hamming_distance(pattern,text[i:i+len(pattern)])] = text[i:i+len(pattern)]
        
    return min(hamming_distances)



