##An an implementation of a tree structure. 
##Trees can be constructed independently or given a file to create the tree from.

from node import *

class Tree:

    def __init__(self):
        self.root = None
    def getRoot(self):
        return self.root
    def setRoot(self, root):
        self.root = root
        return
    def isEmpty(self):
        if self.root == None:
            return True
        else:
            return False
    def makeTree(self, textf1):

##		Creates the tree structure based on input from a file. 
##		elements in brackets represent child nodes
##		Text File Ex: a[b[cd]ef[g]]
##		Represents tree: 
##				     a
##				    /|\
##				   b e f
##				  /\   |
##				 c  d  g
##		Parameters:
##			textfl: a text file
##        that houses a tree data structure
##	tree: an initialized tree structure
##	returns: nothing, -1 if empty file	

        text = open(textf1, "r")
        curr = None
        line = text.readline()

        if len(line) == 0:
            return -1

        nd = Node(line[0])
        self.root = nd
        curr = nd
        place = 1
        
        while (place < len(line)):
            #[-means that the char following it will represent a child node
            #So we create a node for the following char, update the cuerrent node.
            if (line[place] == '['):
                place+=1
                nd = Node(line[place],curr)
                curr.addChild(nd)
                curr = nd
            # ']' this identifies the whole array of children
            
                
            elif line[place]==']':
                curr = curr.getParent()
            else:
                curr = curr.getParent()
                nd = Node(line[place],curr)
                curr.addChild(nd)
                curr = nd
            place +=1
            
    
        return
        

        
