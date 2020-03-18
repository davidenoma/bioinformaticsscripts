
find = input("Give me a character to search for: ")
print(find,type(find))

def fact(n):
    #base case
    if n == 0:
        return 1
    else:
        print(n)
        return n * fact(n-1)

print(fact(5))
        
    
def rec_sum(n):
    if n == 0:
        return 0
    else:
        return n + rec_sum(n-1)
print(rec_sum(4))

def sum_func(n):
    if (n<10):
        return n
    else:
        return n % 10 + sum_func(int(n/10))

print (sum_func(4321))

def word_split(phrase,list_of_words,output = None):
    if output is None:
        output = []
    else:
        for word in list_of_words:
            if phrase.startswith(word):
                output.append(word)
                word_split(phrase[len(word):],list_of_words,output)
    return output
    pass

    
    
