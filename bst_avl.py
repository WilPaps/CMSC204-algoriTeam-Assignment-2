#bst to avl

class Node:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None
        self.height = 1

class BST:
    def insert(self, root, value):
        if root is None:
            #print statement
            return Node(value)
        if value < root.value:
            root.left = self.insert(root.left, value)
        elif value > root.value:
            root.right = self.insert(root.right, value)

        return root #duplicates not allowed
    
class AVL:
    def get_height(self, node):
        if node is None:
            return 0
        return node.height
    
    def get_balance(self, node):
        if node is None:
            return 0
        return self.get_height(node.left) - self.get_height(node.right)
    
    def right_rotation(self, z):
        y = z.left
        T3 = y.right

        #change pointer
        y.right = z
        z.left = T3

        z.height = 1 + max(self.get_height(z.left), self.get_height(z.right))
        y.height = 1 + max(self.get_height(y.left), self.get_height(y.right))

        return y
    
    def left_rotation(self, z):
        y = z.right
        T2 = y.left

        #change pointer
        y.left = z
        z.right = T2

        z.height = 1 + max(self.get_height(z.left), self.get_height(z.right))
        y.height = 1 + max(self.get_height(y.left), self.get_height(y.right))
        
        return y
    
    def insert(self, root, value):
        if root is None:
            return Node(value)
        
        if value < root.value:
            root.left = self.insert(root.left, value)

        elif value > root.value:
            root.right = self.insert(root.right, value)
        
        else:
            return root #duplicates not allowed

        root.height = 1 + max(self.get_height(root.left), self.get_height(root.right))

        balance = self.get_balance(root)

        #left-left rotation
        if balance > 1 and value < root.left.value:
            return self.right_rotation(root)
        #right-right rotation
        if balance < -1 and value > root.right.value:
            return self.left_rotation(root)
        #left-right rotation
        if balance > 1 and value > root.left.value:
            root.left = self.left_rotation(root.left)
            return self.right_rotation(root)
        #right-left rotation 
        if balance < -1 and value < root.right.value:
            root.right = self.right_rotation(root.right)
            return self.left_rotation(root)
        
        return root