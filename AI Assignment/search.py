#Implementation of depth first search
from node import *
from tree import *

import sys

def main():
    if (len(sys.argv) != 2):
        print ("Invalid, need two arguments. e.g. \n\t$ python search.py <textfile.txt>")
        return
    filename = sys.argv[1]

    tree = Tree()
    tree.makeTree(filename)
    print("\nLet's search!")

    find = input("Give me a character to search for: ")
    
    if len(find) > 1:
        print("Sorry that's invalid")
        
    result = DFS(tree,find)

    if result == -1:
        print ("We could not find the element you are looking for. Sorry")
    else:
        print ("Found your node! \n" + str(result))

def DFS(tree,item):
##    This is the implementation of the a dfs algorithm properly 
        stack = []
        curr = tree.getRoot()
        stack.append(curr)

        while len(stack) > 0:
            curr = stack.pop()

            if curr.getData == item:
                
                return curr
            else:
                
                [stack.append(elem) for elem in curr.getChildren()[-1::-1]]

        return -1
    
main()
