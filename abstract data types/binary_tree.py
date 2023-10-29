from sqlalchemy import values


class Node:
    def __init__(self,value):
        self.value = value
        self.left = None
        self.right = None

class Stack:
    def __init__(self):
        self.elements = []

    def push(self, element):
        self.elements.append(element)

    def pop(self):
        try:
            return self.elements.pop()
        except:
            pass

    def isEmpty(self):
        if self.elements:
            return False
        else:
            return True

    def peek(self):
        return self.elements[-1]

class Tree:
    def __init__(self):
        self.root = None
    
    def addrecurse(self,value,currentNode):
        newNode = Node(value)
        if value > currentNode.value:
            if currentNode.right == None:
                currentNode.right = newNode
            else:
                self.addrecurse(value,currentNode.right)
        
        if value < currentNode.value:
            if currentNode.left == None:
                currentNode.left = newNode
            else:
                self.addrecurse(value,currentNode.left) 

    def add(self,value):
        if self.root == None:
            self.root = Node(value)
        else:
            self.addrecurse(value,self.root)
    
    def inorder(self,node):
        #LVR
        if node.left:
            self.inorder(node.left)
        print(node.value, end=' ')
        if node.right:
            self.inorder(node.right)
    
    def preorder(self,node):
        #VLR
        print(node.value, end=' ')
        if node.left:
            self.preorder(node.left)
        if node.right:
            self.preorder(node.right)

    def postorder(self,node):
        #LRV
        if node.left:
            self.preorder(node.left)
        if node.right:
            self.preorder(node.right)
        print(node.value, end=' ')
    
    def remove(self,value,node):
        if node is None:
            return node
        if node.value > value:
            self.remove(self,value,node.left)
        if node.value < value:
            self.remove(self,value,node.right)

        if node.value == node:
            if (node.left is None) and (node.right is None):
                pass


tree = Tree()
tree.add(3)
tree.add(9)
tree.add(2)
tree.add(1)
tree.add(0)
tree.add(6)
tree.add(5)
print(tree.root.right.left.left.value)