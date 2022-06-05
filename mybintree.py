from BinaryTree import inOrderTraversal, preOrderTraversal
from BinaryTreePL import BinaryTree

# we create a binary tree of size 8
newBT = BinaryTree(8)
# root
newBT.insertNode("Drinks")
# left child
newBT.insertNode("Hot")
# right child
newBT.insertNode("Cold")
newBT.insertNode("Tea")
newBT.insertNode("Coffee")

# testing search method
print("Testing the searching method  - looking for 'Tea'")
print(newBT.searchNode("Tea"))

print("\nTesting the preorder traversal")
newBT.preOrderTraversal(1)

print("\nTesting the inorder traversal")
newBT.inOrderTraversal(1)

print("\nTesting the postorder traversal")
newBT.postOrderTraversal(1)