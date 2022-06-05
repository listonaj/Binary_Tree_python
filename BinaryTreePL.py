
class BinaryTree:
    def __init__(self, size):
        # we fix the size of the list at the creation 
        self.customList = size * [None]
        # we reference the last used index set to zero as we skip the first index
        self.lastUsedIndex = 0
        self.maxSize = size
    
    def insertNode(self, value):
        #case where we are at the end of the list
        if self.lastUsedIndex + 1 == self.maxSize:
            return "The Binary Tree is full"
        self.customList[self.lastUsedIndex+1] = value 
        #every time we insert we increase the last used index by 1
        self.lastUsedIndex += 1
        return "The value has been successfully inserted"

    def searchNode(self, nodeValue):
        # traverse the list 
        for i in range(len(self.customList)):
            #compare each element with element we are looking for
            if self.customList[i] == nodeValue:
                return "Good news! the node you are looking for have been found"
        return "The value has not been found, sorry!"
    
    def preOrderTraversal(self, index):
        if index > self.lastUsedIndex:
            return
        print(self.customList[index])
        self.preOrderTraversal(index*2)
        self.preOrderTraversal(index*2 + 1)

    def inOrderTraversal(self, index):
        if index > self.lastUsedIndex:
            return
        self.inOrderTraversal(index*2)
        print(self.customList[index])
        self.inOrderTraversal(index*2+1)
    
    def postOrderTraversal(self, index):
        if index > self.lastUsedIndex:
            return
        self.postOrderTraversal(index*2)
        self.postOrderTraversal(index*2+1)
        print(self.customList[index])
    
    def levelOrderTraversal(self, index):
        for i in range(index, self.lastUsedIndex+1):
            print(self.customList[i])
    
    def deleteNode(self, value):
        if self.lastUsedIndex == 0:
            return "There is not any node to delete"
        for i in range(1, self.lastUsedIndex+1):
            if self.customList[i] == value:
                self.customList[i] = self.customList[self.lastUsedIndex]
                self.customList[self.lastUsedIndex] = None
                self.lastUsedIndex -= 1
                return "The node has been successfully deleted"
    
    def deleteBT(self):
       self.customList = None
       return "The BT has been successfully deleted"

    
 





