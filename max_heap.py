#max heap

#General max heapify function
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

#Convert Part 1 key to Max Heap
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

#Nuetralize highest score
def extract_max(heap):
    if len(heap) == 0:
        return None
    
    if len(heap) == 1:
        return heap.pop()
    
    # Store the maximum value (root)
    max_value = heap[0]
    
    # Move the last element to the root
    heap[0] = heap[-1]
    heap.pop()  # Remove the last element
    
    # Restore heap property
    max_heapify(heap, len(heap), 0)
    
    return max_value

#Get two maximum values
def extract_two_maximum_values(original_heap):
    
    heap = original_heap.copy()
    extracted_values = []
    
    print("Initial Max Heap:")
    print_heap(heap)
    print("-" * 50)
    
    # Extract first maximum
    if len(heap) > 0:
        first_max = extract_max(heap)
        extracted_values.append(first_max)
        
        print(f"Extracted first maximum: {first_max}")
        print("\nHeap after extracting first maximum:")
        if len(heap) > 0:
            print_heap(heap)
        else:
            print("Heap is now empty")
        print("-" * 50)
    
    # Extract second maximum
    if len(heap) > 0:
        second_max = extract_max(heap)
        extracted_values.append(second_max)
        
        print(f"Extracted second maximum: {second_max}")
        print("\nHeap after extracting second maximum:")
        if len(heap) > 0:
            print_heap(heap)
        else:
            print("Heap is now empty")
        print("-" * 50)
    
    print(f"Extracted values in order: {extracted_values}")
    print(f"Remaining heap: {heap}")
    
    return extracted_values, heap

#test data
key = [2,5,3,0,2,0,0,6] #original key
# key_rev = [3,2,5,0,2,6,0,0] #balanced key
key_rev = [2, 0, 3, 0, 0, 2, 5, 6]

#temporary for me to run the file
if __name__ == "__main__":
    print("Original key_rev array:", key_rev)
    print()
    
    #Build max heap from key_rev
    max_heap = build_max_heap_from_key(key_rev)
    
    #Display the results
    print_heap(max_heap)
    
    print("\n" + "="*60)
    
    # Demonstrate extracting two maximum values
    extract_two_maximum_values(max_heap)