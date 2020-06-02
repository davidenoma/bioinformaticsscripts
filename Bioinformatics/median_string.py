#Median String Finding Problem
from hamming_distance import *

DNA = ['AAATTGACGCAT','GACGACCACGTT','CGTCAGCGCCTG','GCTGAGCACCGG','AGTACGGGACAG']
def median_string(DNA,k):
    
    for dnai in DNA:
        print(dnai)
        
        for i in range(len(dnai) - k):
            print(dnai[i:i+k])            
            print(d(dnai[i:i+k],dnai))
    print(minimums,len(minimums))
# median_string(DNA, 3)      

def min_kmer(seq,k):
    for i in range(len(seq) - k):
        
        
min_kmer('AAATTGACGCAT', 3)   
    
    
