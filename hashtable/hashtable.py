
# Edit class to account for re-sizing if insertion or deletion causes
# load size to be too large or small
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
    """

    key_value_pair_counts = 0

    def __init__(self, capacity):
        self.capacity = MIN_CAPACITY
        self.array_buckets = [None for i in range(capacity)]


    def get_num_slots(self):
        """
        Return the length of the list you're using to hold the hash
        table data. (Not the number of items stored in the hash table,
        but the number of slots in the main list.)

        One of the tests relies on this.
        """
        # return the length of the array
        return len(self.array_buckets)


    def get_load_factor(self):
        """
        Return the load factor for this hash table.
        """
        # return load factor
        return HashTable.key_value_pair_counts / self.get_num_slots()


    def djb2(self, key):
        """
        DJB2 hash, 32-bit
        """

        hash = 5381

        byte_array = key.encode('utf-8')

        for byte in byte_array:

            hash = ((hash << 5) + hash) + byte

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
        """

        # check if load factor would become > 0.7 if we add a new entry
        if (HashTable.key_value_pair_counts + 1) / self.get_num_slots() > 0.7:

            # if it would, double size and rehash
            self.resize(2*self.capacity)

        # increment # of pairs in table
        HashTable.key_value_pair_counts += 1

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

        # STRETCH

        # if the load factor would become < 0.2 if we delete an entry
        if (HashTable.key_value_pair_counts - 1) / self.get_num_slots() < 0.2:

            # if our capacity isn't already at minimum
            if not self.capacity == MIN_CAPACITY:

                # resize to half the capacity
                self.resize(int(self.capacity/2))
 
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

                    # remove a pair from our k/v pair counter
                    HashTable.key_value_pair_counts -= 1

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
        # store the existing array
        temp = self.array_buckets

        # set new capacity
        self.capacity = new_capacity

        # reset array to empty
        self.array_buckets = [None for i in range(self.capacity)]

        # reset key value pair counts to 0
        HashTable.key_value_pair_counts = 0

        # for each index in our temp array
        for node in temp: 

            # while a node exists at that index
            while node:
            
                # insert the new node
                self.put(node.key, node.value)

                # go to the next node
                node = node.next


if __name__ == "__main__":
    ht = HashTable(8)

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


    print("")

    # Test storing beyond capacity (only for module 1 testing)
    for i in range(1, 13):
        print(ht.get(f"line_{i}"))
    print(ht.get(f"line_13"))

    # Test resizing
    old_capacity = ht.get_num_slots()
    # ht.resize(ht.capacity * 2)
  
    new_capacity = ht.get_num_slots()


    print(f"\nResized from {old_capacity} to {new_capacity}.\n")
    print("Load factor:", ht.get_load_factor())

    # Test if data intact after resizing
    for i in range(1, 13):
        print(ht.get(f"line_{i}"))

    # print("")

    # ht.delete("line_1")
    # ht.delete("line_2")
    # ht.delete("line_3")
    # ht.delete("line_4")
    # ht.delete("line_5")
    # ht.delete("line_6")
    # ht.delete("line_7")
    # ht.delete("line_8")
    # ht.delete("line_9")
    # ht.delete("line_10")
    # ht.delete("line_11")
    # ht.delete("line_12")
    print("Load factor:", ht.get_load_factor())
    print('capacity:', ht.capacity)
    print('kvpc:', ht.key_value_pair_counts)
