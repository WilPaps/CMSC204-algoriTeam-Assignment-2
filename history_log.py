#History Log

#test data
key = [2, 0, 3, 0, 0, 2, 5, 6]

class AVLNode:
    def __init__(self, key):
        self.key = key
        self.left = None
        self.right = None
        self.height = 1

def print_avl_descending_with_stack(root):
    # Non-recursive stack
    # Reverse in-order traversal: Right -> Root -> Left
    if not root:
        return
    
    stack = []
    current = root
    result = []
    stack_trace = []  # To track first 4 operations
    all_operations = []  
    operation_count = 0
    
    print("Stack-based descending traversal trace:")
    print("=" * 60)
    
    while stack or current:
        # Go to the rightmost node first
        if current:
            stack.append(current)
            stack_contents = [node.key for node in stack]
            operation = f"PUSH: Added node {current.key} to stack | Stack: {stack_contents}"
            all_operations.append(operation)
            
            # Trace first 4 operations
            if operation_count < 4:
                stack_trace.append(operation)
                operation_count += 1
            
            current = current.right
        else:
            # Pop from stack and process
            current = stack.pop()
            stack_contents = [node.key for node in stack] if stack else []
            operation = f"POP:  Removed node {current.key} from stack | Stack: {stack_contents} | VISITED: {current.key}"
            all_operations.append(operation)
            
            # Trace first 4 operations
            if operation_count < 4:
                stack_trace.append(operation)
                operation_count += 1
            
            result.append(current.key)
            
            # Move to left subtree
            current = current.left
    
    # Print trace of first 4 operations
    print("First 4 stack operations:")
    for i, operation in enumerate(stack_trace, 1):
        print(f"{i}. {operation}")
    
    print(f"\n📊 Complete traversal sequence:")
    for i, op in enumerate(all_operations, 1):
        print(f"{i:2d}. {op}")
    
    print(f"\n🎯 Keys in descending order: {result}")
    return result

def create_avl_tree_from_keys(keys=None):
    if keys is None:
        keys = key  # Use the default key array from line 3
    
    print(f"Input key array: {keys}")
    
    if not keys:
        return None
    
    # Build AVL tree by inserting keys in order
    # This creates a more balanced tree structure dynamically
    root = None
    
    for i, k in enumerate(keys):
        root = insert_avl_node(root, k, i)  # Pass index for handling duplicates
    
    return root

def insert_avl_node(root, key, index=0):
    if root is None:
        return AVLNode(key)
    
    # Since the expected key is an AVL tree already, use binary search tree structure
    if key <= root.key:
        root.left = insert_avl_node(root.left, key, index)
    else:
        root.right = insert_avl_node(root.right, key, index)
    
    return root

def demonstrate_stack_traversal(test_keys=None):
    if test_keys is None:
        test_keys = key  # Use default key array from line 3
    
    root = create_avl_tree_from_keys(test_keys)
    
    if key:
        print("🔍 Algorithm Explanation:")
        print("- To get DESCENDING order, we use REVERSE in-order traversal")
        print("- Normal in-order: Left → Root → Right (ascending)")  
        print("- Reverse in-order: Right → Root → Left (descending)")
        print("- Stack simulates recursion: push right path, pop & process, go left")
        print()
        
        print_avl_descending_with_stack(root) #root
    else:
        print("No valid keys found to create tree")


#temporary for me to run the file only
if __name__ == "__main__":
    demonstrate_stack_traversal(key)

