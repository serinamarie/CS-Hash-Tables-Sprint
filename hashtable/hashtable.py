class HashTableEntry:
    """
    Linked List hash table key/value pair
    """
    def __init__(self, key, value):
        self.key = key
        self.value = value
        self.next = None


# Hash table can't have fewer than this many slots
MIN_CAPACITY = 8


class HashTable:
    """
    A hash table that with `capacity` buckets
    that accepts string keys

    Implement this.
    """

    key_value_pairs = 0

    def __init__(self, capacity):
        self.capacity = capacity
        self.array_buckets = [None for i in range(capacity)]


    def get_num_slots(self):
        """
        Return the length of the list you're using to hold the hash
        table data. (Not the number of items stored in the hash table,
        but the number of slots in the main list.)

        One of the tests relies on this.

        Implement this.
        """
        # return the length of the array
        return len(self.array_buckets)


    def get_load_factor(self):
        """
        Return the load factor for this hash table.

        Implement this.
        """
        # return load factor
        return HashTable.key_value_pairs / self.array_buckets


    def djb2(self, key):
        """
        DJB2 hash, 32-bit

        Implement this, and/or FNV-1.
        """

        hash = 5381

        byte_array = key.encode('utf-8')

        for byte in byte_array:

            hash = (hash * 33) + byte

        return hash
        

    def hash_index(self, key):
        """
        Take an arbitrary key and return a valid integer index
        between within the storage capacity of the hash table.
        """
        return self.djb2(key) % self.capacity


    def put(self, key, value):
        """
        Store the value with the given key.
        Hash collisions should be handled with Linked List Chaining.
        Implement this.
        """
        # increment # of pairs in table
        HashTable.key_value_pairs += 1

        # mod hash with length of array
        index = self.hash_index(key)

        # locate the node index
        current_node = self.array_buckets[index]

        # if there is nothing at that index
        if current_node is None:

            # add a new entry
            self.array_buckets[index] = HashTableEntry(key=key, value=value)

        # if there is a key/value at that index
        else:

            # while there is a key/value at that index and that index doesn't contain the key
            while current_node and current_node.key != key: 

                # set the current node to the last known node
                last_node = current_node

                # make the next node the current node
                current_node = current_node.next

            # if input key does not match an existing key
            if not current_node: 
            
                # once there isn't a current node
                # set a pointer from the last known node to the new one created
                last_node.next = HashTableEntry(key=key, value=value)

            # if input key matches an existing key
            elif current_node.key == key:

                # overwrite existing key value
                current_node.value = value


    def delete(self, key):
        """
        Remove the value stored with the given key.
        Print a warning if the key is not found.
        Implement this.
        """
 
        # mod hash with length of array
        index = self.hash_index(key)

        # locate the index
        current_node = self.array_buckets[index]

        # if there is a node at that index
        if current_node:

            # set the latest node to none (will make sense later in the function)
            last_node = None

            # while a key/value pair exists
            while current_node:
                
                # if the node's key matches input key
                if current_node.key == key:

                    # if there is a previous node 
                    if last_node:

                        # set the current node's 'next' equal to our last node's 'next'
                        last_node.next = current_node.next

                    # if this is the first key at that index
                    else: 

                        # the next node is the first node
                        self.array_buckets[index] = current_node.next

                # go to the next key
                last_node = current_node
                current_node = current_node.next

        # if there is nothing at that index
        else:

            # no key found
            print(f"IndexError: There are no keys at that index")


    def get(self, key):
        """
        Retrieve the value stored with the given key.
        Returns None if the key is not found.
        Implement this.
        """
        # mod hash with length of array
        index = self.hash_index(key)

        # locate the index
        current_node = self.array_buckets[index]

        # if there is nothing at that index
        if current_node is None:

            # no key found
            print(f"KeyError: '{key}' not found in hash table")

        # if there is a node at that index
        else:

            # set the latest node to none (will make sense later in the function)
            last_node = None

            # while a key/value pair exists and that pair is not our input pair
            while current_node and current_node.key != key:
                
                # go to the next key
                last_node = current_node
                current_node = current_node.next
            
            # if loop stopped because we have no more keys to search through
            if not current_node: 

                # no key found
                print(f"KeyError: '{key}' not found in hash table")

            # if loop stopped because found key equal to input key!
            elif current_node.key == key:

                    return current_node.value


    def resize(self, new_capacity):
        """
        Changes the capacity of the hash table and
        rehashes all key/value pairs.

        Implement this.
        """
        # Your code here



if __name__ == "__main__":
    ht = HashTable(8)

    ht.put("key-0", "val-0")
    ht.put("key-1", "val-1")
    ht.put("key-2", "val-2")
    ht.put("key-3", "val-3")
    ht.put("key-4", "val-4")
    ht.put("key-5", "val-5")
    ht.put("key-6", "val-6")
    ht.put("key-7", "val-7")
    ht.put("key-8", "val-8")
    ht.put("key-9", "val-9")
    ht.delete("key-7")
    ht.delete("key-6")
    ht.delete("key-5")
    ht.delete("key-4")
    ht.delete("key-3")
    ht.delete("key-2")
    ht.delete("key-1")
    ht.delete("key-0")
    return_value = ht.get("key-0")
    print("Get value (should be none):", return_value)

    print(ht.djb2("line_1"))
    print(ht.hash_index('line_1'))
    ht.put("line_1", "'Twas brillig, and the slithy toves")
    ht.put("line_2", "Did gyre and gimble in the wabe:")
    ht.put("line_3", "All mimsy were the borogoves,")
    ht.put("line_4", "And the mome raths outgrabe.")
    ht.put("line_5", '"Beware the Jabberwock, my son!')
    ht.put("line_6", "The jaws that bite, the claws that catch!")
    ht.put("line_7", "Beware the Jubjub bird, and shun")
    ht.put("line_8", 'The frumious Bandersnatch!"')
    ht.put("line_9", "He took his vorpal sword in hand;")
    ht.put("line_10", "Long time the manxome foe he sought--")
    ht.put("line_11", "So rested he by the Tumtum tree")
    ht.put("line_12", "And stood awhile in thought.")
    print("Get", ht.get("line_1"))
    print("Delete", ht.delete("line_5"))
    print("")

    # Test storing beyond capacity
    for i in range(1, 13):
        print(ht.get(f"line_{i}"))

    # Test resizing
    old_capacity = ht.get_num_slots()
    ht.resize(ht.capacity * 2)
    new_capacity = ht.get_num_slots()

    print(f"\nResized from {old_capacity} to {new_capacity}.\n")

    # Test if data intact after resizing
    for i in range(1, 13):
        print(ht.get(f"line_{i}"))

    print("")
