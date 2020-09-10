import random

# Read in all the words in one go
with open("input.txt") as f:
    words = f.read()

# TODO: analyze which words can follow other words
#split text into words
# state the stop words
# figure out which words come after a word, get the probabilities of each of those


# TODO: construct 5 random sentences
# Your code here

# separate words into a list
# for each word, put into a dictionary, 
# then create a dict at each key, containing 'next word_ex' as key
# and value being some count / sum(nest_dict.values()) for each vwith the +1 index as value

D = {
    'and': 
        {
            'dogs': 1,
            'birds': 2,
            'fish': 2
        },
    'cats':
        {
            'and': 1,
            'if': 2
        }
}

print(sum(len(v) for v in iter(D['cats'])))
print(D.values())
# print(D)