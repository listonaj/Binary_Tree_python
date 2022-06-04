# Romain Jean-Marc
# 06/04/2022
# basic tree creation follow the drinks tree example from pdf 'trees generalities' 

class Tree_Node:
    def __init__(self, data, children = []):
        self.data = data
        self.children = children
    
    def __str__(self, level=0):
        ret = "  " * level + str(self.data)  + "\n"
        for child in self.children:
            ret += child.__str__(level + 1)
        return ret
    
    def add_Child(self, TreeNode):
        self.children.append(TreeNode)

tree = Tree_Node('Drinks', [])
cold = Tree_Node('Cold', [])
hot = Tree_Node('Hot', [])
tree.add_Child(cold)
tree.add_Child(hot)
tea = Tree_Node('Tea', [])
coffee = Tree_Node('Coffee', [])
cola = Tree_Node('Cola', [])
fanta = Tree_Node('Fanta', [])
cold.add_Child(cola)
cold.add_Child(fanta)
hot.add_Child(tea)
hot.add_Child(coffee)
print(tree)