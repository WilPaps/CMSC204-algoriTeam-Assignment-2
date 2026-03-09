#max heap

def max_heapify(arr, n, i):
    largest = i  # Initialize largest as root
    left = 2 * i + 1  # left child
    right = 2 * i + 2  # right child
    
    if left < n and arr[left] > arr[largest]:
        largest = left
    
    if right < n and arr[right] > arr[largest]:
        largest = right
    
    if largest != i:
        arr[i], arr[largest] = arr[largest], arr[i]
        max_heapify(arr, n, largest)

def build_max_heap_from_key(balanced_key):
    # Create a copy of key from AVL to avoid modifying the original
    heap = balanced_key.copy()
    n = len(heap)
    
    # Build heap (rearrange array)
    for i in range(n // 2 - 1, -1, -1):
        max_heapify(heap, n, i)
    
    return heap

def print_heap(heap):
    print("Max-Heap:", heap)
    
    # Print heap as a tree
    print("\nHeap structure:")
    n = len(heap)
    for i in range(n):
        left_child = 2 * i + 1
        right_child = 2 * i + 2
        
        print(f"Node {i} (value: {heap[i]})")
        if left_child < n:
            print(f"  Left child: {heap[left_child]}")
        if right_child < n:
            print(f"  Right child: {heap[right_child]}")
        print()

#test data
key = [2,5,3,0,2,0,0,6] #original key
key_rev = [3,2,5,0,2,6,0,0] #balanced key

if __name__ == "__main__":
    print("Original key_rev array:", key_rev)
    print()
    
    #Build max heap from key_rev
    max_heap = build_max_heap_from_key(key_rev)
    
    #Display the results
    print_heap(max_heap)