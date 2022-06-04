# Romain Jean-Marc
# 06/04/2022
# basic tree creation follow the drinks tree example from pdf 'trees generalities' 

class Tree_Node:
    # constructor contains data and a link to its children node(list)
    def __init__(self, data, childnodelist = []):
        self.data = data
        self.childnodelist = childnodelist
    
    # added a build in function thaty will print the tree as appearing
    def __str__(self, level=0):
        ret = "  " * level + str(self.data)  + "\n"
        for child in self.childnodelist:
            ret += child.__str__(level + 1)
        return ret
    
    # method to add a node in the tree
    def add_child(self, TreeNode):
        self.childnodelist.append(TreeNode)

