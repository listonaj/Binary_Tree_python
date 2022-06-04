from BinaryTree import*

# create my binary tree with the root
mybintree = TreeNode("Drinks")

# create my nodes childs of the root
leftChild = TreeNode("Hot")
rightChild = TreeNode("Cold")
# put the node position in the binary tree
mybintree.leftChild = leftChild
mybintree.rightChild = rightChild

# create two other nodes
tea = TreeNode("Tea")
coffee = TreeNode("Coffee")
leftChild.leftChild = tea
leftChild.rightChild = coffee

#test the preorder traversal method
print("\ntetsting the preorder traversal algorithm")
preOrderTraversal(mybintree)

#test inorder traversal
print("\ntesting the indorder traversal algorithm")
inOrderTraversal(mybintree)