# Your code here
import random
import math


def slowfun_too_slow(x, y):

    # let v be x ^ y
    v = math.pow(x, y)

    # let v be v*(v-1)*(v-2)...(v-n) where (v-n) = 1
    v = math.factorial(v)


    # set v equal to the floor division result of the sum of x and y
    v //= (x + y)

    # let v be the remainder of v / 982451653
    v %= 982451653

    return v


# create empty dict
lookup_table = {}

def slowfun(x, y):
    """
    Rewrite slowfun_too_slow() in here so that the program produces the same
    output, but completes quickly instead of taking ages to run.
    """

    # if key in dict:
    if (x,y) in lookup_table:

        # return value
        return lookup_table.get(x,y)

    # if key not in dict, create key/value pair
    else:

        # let v be x ^ y
        v = math.pow(x, y)

        # let v be v*(v-1)*(v-2)...(v-n) where (v-n) = 1
        v = math.factorial(v)

        # set v equal to the floor division result of the sum of x and y
        v //= (x + y)

        # let v be the remainder of v / 982451653
        v %= 982451653

        # add key/value pair to dict
        lookup_table[(x,y)] = v
        
        # return value
        return v


# ELI5
# store values in a lookup table as there are far less combinations
# than the range, so we're bound to have the same x,y combo 
# again and again(1k~ times each)

# pseudocode
   # if x,y combo in dict: 
        # return value v for that x,y key
    # if not in dict:
        # do the slow stuff
        # append x,y combo and v to dict
    # return v

# Review: runs in 5 seconds

# Do not modify below this line!

for i in range(50000):
    x = random.randrange(2, 14)
    y = random.randrange(3, 6)
    print(f'{i}: {x},{y}: {slowfun(x, y)}')

# if __name__ == "__main__":

#     for i in range(5):
#         x = random.randrange(2, 14)
#         y = random.randrange(3, 6)
#         print(f'{i}: {x},{y}: {slowfun(x, y)}')

    # x = 5
    # y = 4
    # v = x + y
    # z = 1
    # lookup_table = {(x,y): v}
    # if (x,z) in lookup_table:
    #     print(lookup_table.get((x,y)))
