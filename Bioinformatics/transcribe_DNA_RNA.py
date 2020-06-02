file = open('rosalind_rna.txt','r')
numA =  numC =  numG = numT = 0
pattern = file.read()

newPattern = ''
for char in pattern:
    
    if (char == 'T'):
        newPattern += 'U'
    elif (char == '\n'):
        continue
    else:
        newPattern+=char
print(newPattern)
file.close()
