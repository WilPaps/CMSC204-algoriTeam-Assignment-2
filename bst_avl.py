#bst to avl
from collections import deque

#utility functions

def tree_snapshot(root, label ="Tree"):
    if root is None:
        print(f"[{label}] Tree is empty")
        return
    snapshot = []
    queue = deque([root])
    while queue:
        node = queue.popleft()
        snapshot.append(node.value)
        if node.left:
            queue.append(node.left)
        if node.right:
            queue.append(node.right)

    print(f"[{label}] snapshot: {snapshot}")
    print("-" * 50)

def print_balance_factors(node, avl_instance):
    if node is None:
        return
    print_balance_factors(node.left, avl_instance)
    print(f"Node {node.value} -> Balance Factor {avl_instance.get_balance(node)}")
    print_balance_factors(node.right, avl_instance)

class Node:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None
        self.height = 1

class BST:
    def insert(self, root, value):
        if root is None:
            print(f"[BST] Inserted {value}")
            return Node(value)
        if value <= root.value:    #duplicates go left
            root.left = self.insert(root.left, value)
        else: 
            root.right = self.insert(root.right, value)
        
        tree_snapshot(root, label="BST")
        return root 
    
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

        print(f"[AVL] Right rotation (LL) at node {z.value}")
        tree_snapshot(y, label="AVL")
        return y
    
    def left_rotation(self, z):
        y = z.right
        T2 = y.left

        #change pointer
        y.left = z
        z.right = T2

        z.height = 1 + max(self.get_height(z.left), self.get_height(z.right))
        y.height = 1 + max(self.get_height(y.left), self.get_height(y.right))

        print(f"[AVL] Left rotation (RR) at node {z.value}")
        tree_snapshot(y, label="AVL")
        return y
    
    def insert(self, root, value):
        if root is None:
            print(f"[AVL] Inserted {value}")
            return Node(value)
        
        if value <= root.value:
            root.left = self.insert(root.left, value)

        else: 
            root.right = self.insert(root.right, value)
        

        root.height = 1 + max(self.get_height(root.left), self.get_height(root.right))

        balance = self.get_balance(root)

        #left-left rotation
        if balance > 1 and value <= root.left.value:
            return self.right_rotation(root)
        #right-right rotation
        if balance < -1 and value > root.right.value:
            return self.left_rotation(root)
        #left-right rotation
        if balance > 1 and value > root.left.value:
            print(f"[AVL] Left-Right rotation at node {root.value}")
            root.left = self.left_rotation(root.left)
            return self.right_rotation(root)
        #right-left rotation 
        if balance < -1 and value < root.right.value:
            print(f"[AVL] Right-Left rotation at node {root.value}")
            root.right = self.right_rotation(root.right)
            return self.left_rotation(root)
        
        print("[AVL] Balance factors after insertion: ")
        print_balance_factors(root, self)
        tree_snapshot(root, label="AVL")
        return root

if __name__ == "__main__":

    student_id = input("Enter last 7 digits of your student ID:")
    lastname = input("Enter your last name: ")
    keys = [int(d) for d in student_id[-7:]]
    keys.append(len(lastname))
    print(f"\nGenerated key set (threat severity scores): {keys}\n")

    bst = BST()
    bst_root = None
    print("=== BST Construction ===")
    for k in keys:
        bst_root = bst.insert(bst_root, k)

    avl = AVL()
    avl_root = None
    print("\n=== AVL Balancing ===")
    for k in keys:
        avl_root = avl.insert(avl_root, k)
    