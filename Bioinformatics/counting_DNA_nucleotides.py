file = open('rosalind_dna.txt','r')
numA =  numC =  numG = numT = 0
pattern = file.read()
print(pattern)
for char in pattern:
    
    if (char == 'A'):
        numA = numA + 1
    elif (char == 'C'):
        numC = numC + 1
    elif (char == 'G'):
        numG = numG + 1
    elif(char== 'T'):
        numT = numT + 1
    else:
        continue
print(numA, numC, numG, numT)
