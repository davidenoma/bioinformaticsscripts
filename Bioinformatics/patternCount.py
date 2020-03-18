# -*- coding: utf-8 -*-
"""
Created on Wed Jan 15 12:35:12 2020

@author: kora
"""

def patternCount(seq,pattern):
    count = 0
    lenPattern = len(pattern) -1 
    for i in range(len(seq) - lenPattern):            
        if(seq[i:(i+len(pattern))] == pattern):
            count += 1
    return count

print(patternCount("ATTCGGCTGCGCCC","GCG"))

def frequentWords(text, k):
    frequentPatterns = set()
    count = []
    for i in range(len(text) - k):
            pattern = text[i:i+k]
            count.append(patternCount(text,pattern))
    maxCount = max(count)
    
    for i in range(len(text) - k):
        if (count[i] == maxCount):
            frequentPatterns.add(text[i:k])
    
    return frequentPatterns
print(frequentWords("ATTATTCGGCTGCGCCC",3))