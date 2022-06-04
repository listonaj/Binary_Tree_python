from Create_Tree import*

#create 3 nodes
tree = Tree_Node('Drinks', [])
cold = Tree_Node('Cold', [])
hot = Tree_Node('Hot', [])
# give two childs to the root's tree(does not have parents)... 
# which will imply that tree is... 
# the root node as the two other nodes created have been 
# labelled root's childs
tree.add_child(cold)
tree.add_child(hot)
tea = Tree_Node('Tea', [])
coffee = Tree_Node('Coffee', [])
cola = Tree_Node('Cola', [])
fanta = Tree_Node('Fanta', [])
cold.add_child(cola)
cold.add_child(fanta)
hot.add_child(tea)
hot.add_child(coffee)
print(tree)