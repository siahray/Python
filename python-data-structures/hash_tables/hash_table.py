class HashTable:
    def __init__(self, size=10):
        # We create a list of empty lists. 
        # The inner lists allow us to store multiple items at the same index if a "collision" happens.
        self.table = [[] for _ in range(size)]

    def _hash(self, key):
        # A basic hash function: sums the ASCII values of the characters and uses modulo
        hash_value = sum(ord(char) for char in key) % len(self.table)
        print(f"  [Hash Engine] Key '{key}' converted to index: {hash_value}")
        return hash_value

    def set_item(self, key, value):
        print(f"\nSetting item: '{key}' -> '{value}'")
        index = self._hash(key)
        
        # Check if the key already exists and update it
        for i, kv in enumerate(self.table[index]):
            if kv[0] == key:
                self.table[index][i] = [key, value]
                print(f"  -> Updated existing key at index {index}")
                return
                
        # If it doesn't exist, append it to the list at that index
        self.table[index].append([key, value])
        print(f"  -> Stored at index {index}")

    def get_item(self, key):
        print(f"\nRetrieving item: '{key}'")
        index = self._hash(key)
        
        # Search through the list at that specific index
        for kv in self.table[index]:
            if kv[0] == key:
                print(f"  -> Found value: '{kv[1]}'")
                return kv[1]
                
        print("  -> Key not found!")
        return None

# --- Test the Hash Table ---
print("--- Starting Hash Table Operations ---")
my_hash = HashTable(size=5) # Small size to force collisions intentionally

# Storing data
my_hash.set_item("apple", 100)
my_hash.set_item("banana", 200)
my_hash.set_item("grape", 300) # Watch what index this gets!

# Retrieving data
my_hash.get_item("apple")
my_hash.get_item("grape")

# Print the underlying array to see how data is actually stored
print("\n--- The Raw Hash Table Memory ---")
for idx, bucket in enumerate(my_hash.table):
    print(f"Index {idx}: {bucket}")