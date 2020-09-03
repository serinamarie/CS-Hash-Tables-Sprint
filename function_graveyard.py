def delete3(self, key):
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

        # while a key/value pair exists and that pair is not our input pair
        while current_node and current_node != key:

            # go to the next key
            last_node = current_node
            current_node = current_node.next

        # once there is no next node or the current node key matches the input key
        # if the current node key matches the input key
        try:
            if current_node.key == key:

                # if there is a previous node 
                if last_node:

                    # set the current node's 'next' equal to our last node's 'next'
                    last_node.next = current_node.next

                # if there isn't a previous node (this is the first node)
                else:

                    # the next node is the first node
                    self.array_buckets[index] = current_node.next
            
            # if the current node key does not match the input key
            else:

                # no key found
                print(f"KeyError: '{key}' not FOUND in hash table")
    
    # if there is nothing at that index
    else:

        # no key found
        print(f"IndexError: There is no key at that index")
    
    
            


        
            # if it is the right key
            elif current_node.key == key:

                # if there is a previous node 
                if last_node:
                    
                    # set the current node's 'next' equal to our last node's 'next'
                    last_node.next = current_node.next

                # if there isn't a previous node (this is the first node)
                else:

                    # the next node is the first node
                    self.array_buckets[index] = current_node.next

        decrement the number of pairs
        key_value_pairs -= 1


def delete2(self, key):
    """
    Remove the value stored with the given key.

    Print a warning if the key is not found.

    Implement this.
    """
    # hash the key 
    hash_1 = self.djb2(key)

    # mod hash with length of array
    index = hash1 % self.capacity

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

        # while there is a key/value pair
        while current_node:

            # if it is the right key
            if current_node.key == key:

                # if there is a previous node 
                if last_node:
                    
                    # set the current node's 'next' equal to our last node's 'next'
                    last_node.next = current_node.next

                # if there isn't a previous node (this is the first node)
                else:

                    # the next node is the first node
                    self.array_buckets[index] = current_node.next
    
            # if it doesn't have the right key
            else:

                # go to the next key
                last_node = current_node
                current_node = current_node.next

        once there is no current node
        if last_node.key == key:

    decrement the number of pairs
    key_value_pairs -= 1

def get2(self, key):
        """
        Retrieve the value stored with the given key.

        Returns None if the key is not found.

        Implement this.
        """
        # hash the key 
        hash_1 = self.djb2(key)

        # mod hash with length of array
        index = hash_1 % self.capacity

        # locate the node index
        current_node = self.array_buckets[index]

        # if there is nothing at that index
        if current_node is None:

            # return error
            return None

        # if there is a key/value at that index
        else:

            # while there is a key/value at that index
            while current_node: 

                if current_node.key == key:

                    return current_node.value
                
                # if this node's key isn't the right key
                else:

                    # set the current node to the last known node
                    last_node = current_node

                    # make the next node the current node
                    current_node = current_node.next