import numpy as np

class Node:

    def __init__(self, data):

        self.left = None
        self.right = None
        self.data = data

    def insert(self, data):
        if self.data:
            
            if data < self.data:
                #print("left tree", self)
                if self.left is None:
                    print("left child",self)
                    self.left = Node(data)
                else:
                    self.left.insert(data)
            elif data > self.data:
                #print("right tree", self)
                if self.right is None:
                    print("right child",self)
                    self.right = Node(data)
                else:
                    self.right.insert(data)

        else:
            self.data = data

    def get_right_child(self):
        return self.right
    def get_left_child(self):
        return self.left
    def set_root_val(self, rootVal):
        self.data = rootVal
    def get_root_val(self):
        return self.data
    def inorder_traversal(self):
        if self.left:
            self.left.inorder_traversal()
        print(self.data)
        if self.right:
            self.right.inorder_traversal()
    def preorder_traversal(self):
        print(self.data)
        if self.left:
            self.left.preorder_traversal()
        if self.right:
            self.right.preorder_traversal()
            
    def postorder_traversal(self):
        if self.left:
            self.left.postorder_traversal()
        if self.right:
            self.right.postorder_traversal()
        print(self.data)

print("The binary will be created with your numbers.")

root = None

print("Please enter 10 numbers to create sorted binary tree.")
for i in range(0,9):
    val = int(input("Please enter a number: "))
    if i == 0:
        root = Node(val)
        #root.set_root_val(val)
        #root = Node(val)
        print("root: None")
    else:
        root.insert(val)
        print("root: ", root.get_root_val())
print("...***...\nPre-Order")
root.preorder_traversal()
print("...***...\nPost-Order")
root.postorder_traversal()
print("...***...\nIn-Order")
root.inorder_traversal()
