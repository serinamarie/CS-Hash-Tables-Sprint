### Lecture 1
Hash functions: takes string, returns int. Usually operate on the bytes that make up a string. Deterministic

Pseudocode for put
1. hash the key
2. take the hash and mod it with the len of array
3. Go to index and put in value

Pseudocode for get
1. hash the key
2. take the hash and mod it with the len of array
3. Go to index and get out the value

Time complexity?
- Same for get and put
- Linear in length of string/key
- Constant time in length of array <------ This is important part
O(1)

```python
    #Collision
    key1='dad'
    key2='add'

    #Put 1
    hash1=UTF8_hash(key1)
    idx1 = has1 % len(my_arr2)
    my_arr2[idx] = 'howdy'

    #Put 2
    hash2=UTF8_hash(key2)
    idx2 = hash2 % len(my_arr2)
    my_arr2[idx2] = 'whats up yall'

    get_hash = UTF8_Hash(key1)
    idx3 = get_hash % len(my_arr2)
    print(my_arr2[idx3])
```

## Collision Resolution

Open addressing 

    - Linear probing: if index is unavailable, go to next available empty index

        - Cons w/ linear probing:

        - primary clustering: keys might bunch together

    - Plus 3 rehash

    - Quadratic probing (failed attempts)^2 (if failed attempt, square to get even further away)

    - Double hashing 

- Pros of open addressing:

    - If load factor is low, better to use open addressing


Closed addressing

Chaining (also called closed addressing)

- Put: All keys are added as a node to a link list (so some indices will have multiple keys)

- Get: calculate index, linked list traversal to find

- Pros:

    - Quicker lookup

    - If load factor is high this might be better


1. set a constant hash = 5381
2. for letter in string
3. hash = g* hash + s.char(letter)
2. return hash

```python
def djb2(s):
    hash = 5381
    byte_array = s.encode('utf-8')
    for byte in byte_array:
        hash = (hash * 33) + byte


hash = (hash*33) + byte
oooor xor
hash = hash(byte-1) * 33^byte

hash(i) = hash(i - 1) * 33 ^ str[i]
```

## Lecture 3
1. which is faster, adding to head, or add to tail? it doesn't matter(?) 
You always have to iterate through all keys.

amortize the cost of resizing over all the puts
resizing is rare, because we double in size
basically it's O(1)

Probably best to use the built-in dict type

### Pattern matching 
Module 3 and 4 are to provide practice in spotting problems that might require a hash table

- Consider your data structure: array, tree, hash table?

- Time complexity is easy to think about with arrays v hash tables

- Use hash tables when you reaquiring information would be too slow. And if you have something you need to look up quickly
compared to alternatives (esp when slower methods would cause a problem)
    - linear search of an array
    - if you search for something in an array, and store the info in a hashtable so when you return to look up that info you could look
    at the hashtable first 

- Dynamic programming

- Code up a function
    - make a function that will returnt he n-th element of the Fibonacci sequence
    - apply UPER
        - Understand
            - Feynman technique
                - ELI5 
        - Plan
            - pseudocode that you can execute
            - Use a recursive solution (find n-1 and n-2 things)
            - base case (the two we started off with (0 and 1))
            - function calls itself
            - progress toward base case
            - return fib of n-1 and fib of n-2, summed
        - Execute

    ```python
    def fibonacci(n):
        # base case
        ### 0 and/or 1
        if n <= 1:
            return n

        return fibonacci(n-1) + fibonacci(n-2)
        ```

            - if you discover an edge case or something, throw it in your plan
            
        - Review

- What is the time complexity of this function? Exponential O(c^n)

- Improve time complexity using memoization
    - check if we have a result before doing the memoization

    ```python
    memo = {}
    def memoized_fibonacci(n):

        # base case (0 and/or 1)
        if n <= 1:
            return n

        # check if we have a result before doing the computation
        if n in memo:
            return memo[n]
    
        # store results as we go
        else: 
            memo[n] = fibonacci(n-1) + fibonacci(n-2)
    
        # progress toward base case
        # return fib of n-1 and fib of n-2, summed 
        return memo[n]

    memoized_fibonacci(3) # should be 2
    memoized_fibonacci(2) + memoized_fibonacci(1)
    memoized_fibonacci(1) + memoized_fibonacci(0)

    print(memoized_fibonacci(12))
    ```
