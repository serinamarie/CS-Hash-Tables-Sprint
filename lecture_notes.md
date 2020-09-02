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

```
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
