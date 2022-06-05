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

# test the preorder traversal method
print("\ntetsting the preorder traversal algorithm")
preOrderTraversal(mybintree)

# test inorder traversal
print("\ntesting the indorder traversal algorithm")
inOrderTraversal(mybintree)

#test postorder traversal
print("\ntesting the postorder traversal algorithm")
postOrderTraversal(mybintree)

#test the levelorder traversal
print("\ntesting the level order traversal algorithm")
levelOrderTraversal(mybintree)

#test the seach method
print("\nTesting the searchBT() method")
print(searchBT(mybintree, "Tea"))
print(searchBT(mybintree,"Dr Pepper"))

#test the insert method
print("\ntrying to insert the node 'Dr pepper in the tree")
# create a new node to insert in the tree
newNode = TreeNode("Dr Pepper")
print(insertNodeBT(mybintree, newNode))
# check if the node has been inserted by printing the tree
preOrderTraversal(mybintree)


