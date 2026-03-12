# main - compile everything here

from bst_avl import BST, AVL, tree_snapshot, print_balance_factors
from max_heap import build_max_heap_from_key, extract_two_maximum_values, print_heap
from blacklist import HastTable
#input generate key
#history log stack descending traversal

def run_bst_avl(keys):
    print("=== Part 1: BST Construction and AVL Balancing ===\n")

    bst = BST()
    bst_root = None
    print("BST Construction")
    for k in keys:
        bst_root = bst.insert(bst_root, k)

    avl = AVL()
    avl_root = None
    print("AVL Balancing")
    for k in keys:
        avl_root = avl.insert(avl_root, k)
    
    return bst_root, avl_root, avl

def run_max_heap(keys):
    print("\n=== Part 2: Max Heap (Priority Attack Queue) ===\n")
    heap = build_max_heap_from_key(keys)
    print_heap(heap)
    extract_two_maximum_values(heap)

def run_hash_table(keys):
    print("\n=== Part 2: IP Blacklist (Hash Table) ===\n")
    hash_table = HashTable()
    for key in keys:
        hash_table.insert(key)
        hash_table.display_table()
    hash_table.display_collision_summary()
    return hash_table

#def run_history_log

def run_all(keys):
    bst_root, avl_root, avl_instance = run_bst_avl(keys)
    run_max_heap(keys)
    run_hash_table(keys)
    run_history_log(avl_root, avl_instance)

def main_menu():
    keys = get_student_keys()

    while True:
        print("\n=== Sentinel System Menu ===")
        print("1. Part 1 - BST & AVL")
        print("2. Part 2a - Max Heap")
        print("3. Part 2b - IP Blacklist")
        print("4. Part 3 - History Log (AVL)")
        print("5. Run Entire System")
        print("0. Exit")

        choice = input("Enter your choice: ").strip()
        if choice == "1":
            run_bst_avl(keys)
        elif choice == "2":
            run_max_heap(keys)
        elif choice == "3":
            run_hash_table(keys)
        elif choice == "4":
            #history
        elif choice == "5":
            run_all(keys)
        elif choice == "0":
            print("Exiting sentinel system...")
            break
        else:
            print("Invalid choice. Enter a number 0-5.")

if __name__ == "__main__":
    main_menu()

