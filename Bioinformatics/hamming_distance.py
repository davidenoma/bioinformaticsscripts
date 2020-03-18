# -*- coding: utf-8 -*-
"""
Created on Wed Jan 15 12:34:07 2020

@author: kora
"""

def hamming_distance(s1,s2):
#    Hamming is the total numper of positions
#    where in the two nucleotide sequences differ.
    if len(s1) != len(s2):
        raise ValueError("Undefined for sequences of unequal length");
    return sum(ch1 != ch2 for ch1, ch2 in zip(s1,s2))
seq1="CAGAAAGGAAGGTCCCCATACACCGACGCACCAGTTTA"
seq2="CACGCCGTATGCATAAACGAGCCGCACGAACCAGAGAG" 

print (hamming_distance(seq1, seq2))

#[(x,y) for x in [1,2,3,4]]
def approximatePatternCount(text,pattern,d):
    count = 0 
    for i in range(len(text)-len(pattern)):
        approxPattern = text[i:i+len(pattern)]
        
        if(hamming_distance(pattern,approxPattern) <= d):
#            print(approxPattern)
            count +=1
    return count

     
approximatePatternCount("TACGCATTACAAAGCACA","AA",1)

