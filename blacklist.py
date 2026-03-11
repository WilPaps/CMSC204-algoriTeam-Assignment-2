#IP blacklist - hashing

#test data
key_rev = [3,2,5,0,2,6,0,0] #balanced key

class HashTable:
    def __init__(self, size=11):
        self.size = size
        self.table = [None] * size
        self.collision_details = []
    
    def hash_function(self, key): #h(k) = k mod 11
        return key % self.size
    
    def quadratic_probe(self, key, i): #h(k,i) = (h(k) + 3i^2 + 2) mod 11
        initial_hash = self.hash_function(key)
        return (initial_hash + 3 * (i ** 2) + 2) % self.size
    
    def insert(self, key):
        initial_pos = self.hash_function(key)
        
        print(f"\nInserting key: {key}")
        print(f"Initial hash: h({key}) = {key} mod {self.size} = {initial_pos}")
        
        # Check if initial position is free
        if self.table[initial_pos] is None:
            self.table[initial_pos] = key
            print(f"✓ Inserted {key} at index {initial_pos}")
            return True
        
        # Handle collision using quadratic probing
        print(f"✗ COLLISION! Index {initial_pos} is already occupied by {self.table[initial_pos]}")
        
        collision_info = {
            'key': key,
            'initial_hash': initial_pos,
            'attempts': []
        }
        
        # Quadratic probing
        for i in range(1, self.size):  # Try up to table size attempts
            probe_pos = self.quadratic_probe(key, i)
            calculation = f"h({key},{i}) = ({initial_pos} + 3({i})² + 2) mod {self.size}"
            calculation += f" = ({initial_pos} + {3 * (i ** 2)} + 2) mod {self.size}"
            calculation += f" = {initial_pos + 3 * (i ** 2) + 2} mod {self.size} = {probe_pos}"
            
            print(f"  Attempt {i}: {calculation}")
            
            collision_info['attempts'].append({
                'attempt': i,
                'calculation': calculation,
                'position': probe_pos,
                'occupied': self.table[probe_pos] is not None
            })
            
            if self.table[probe_pos] is None:
                self.table[probe_pos] = key
                print(f"  ✓ Inserted {key} at index {probe_pos}")
                collision_info['final_position'] = probe_pos
                collision_info['success'] = True
                self.collision_details.append(collision_info)
                return True
            else:
                print(f"  ✗ Index {probe_pos} is occupied by {self.table[probe_pos]}")
        
        # If we get here, no empty slot was found
        print(f"  ✗ Failed to insert {key} - no empty slot found after {self.size-1} attempts")
        collision_info['success'] = False
        self.collision_details.append(collision_info)
        return False
    
    def display_table(self):
        print(f"\n{'='*50}")
        print("HASH TABLE STATE (Size = 11)")
        print(f"{'='*50}")
        for i in range(self.size):
            if self.table[i] is not None:
                print(f"Index {i:2d}: {self.table[i]}")
            else:
                print(f"Index {i:2d}: [EMPTY]")
        print(f"{'='*50}")
    
    def display_collision_summary(self):
        if not self.collision_details:
            print("\nNo collisions occurred during insertion.")
            return
        
        print(f"\n{'='*60}")
        print("COLLISION RESOLUTION SUMMARY")
        print(f"{'='*60}")
        
        for detail in self.collision_details:
            print(f"\nKey {detail['key']}:")
            print(f"  Initial hash position: {detail['initial_hash']} (occupied)")
            for attempt in detail['attempts']:
                status = "SUCCESS" if not attempt['occupied'] else "COLLISION"
                print(f"  {attempt['calculation']} - {status}")
                if not attempt['occupied']:
                    break
            
            if detail['success']:
                print(f"  ✓ Final position: {detail['final_position']}")
            else:
                print(f"  ✗ FAILED - No empty slot found")

def demonstrate_hash_table_insertion():
    print("HASH TABLE IMPLEMENTATION WITH CUSTOM QUADRATIC PROBING")
    print("="*70)
    print(f"Key array to insert: {key_rev}")
    print(f"Hash table size M = 11")
    print(f"Initial hash function: h(k) = k mod 11")
    print(f"Quadratic probing collision resolution: h(k,i) = (h(k) + 3i² + 2) mod 11")
    print("="*70)
    
    # Create hash table
    hash_table = HashTable(11)
    
    # Insert each key from key_rev
    for key in key_rev:
        success = hash_table.insert(key)
        hash_table.display_table()
    
    # Display collision summary
    hash_table.display_collision_summary()
    
    return hash_table

#temporary for me to run the file only
if __name__ == "__main__":
    demonstrate_hash_table_insertion()

