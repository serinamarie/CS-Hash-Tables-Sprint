import numpy as np

# Read in all the words in one go

filename = 'input.txt'
# def markovify(filename):

with open(filename) as f:
    words = f.read()
    corpus = words.split()

def get_current_and_next(word_list):

    # for each word in our word list
    for i in range(len(word_list) - 1):

        # iterate over without storing
        # can produce a sequence of values
        yield (word_list[i], word_list[i+1])

current_and_next = get_current_and_next(corpus)

d = {}

# grab the two values from the gen obj
for current_word, next_word in current_and_next:

    # if current word is already a key
    if current_word in d.keys():

        # add another 'next' word
        d[current_word].append(next_word)
    else:

        # create a key where value is a list of next words 
        d[current_word] = [next_word]

num_of_words = 75


# generate a start word
start_word = np.random.choice(corpus)

# create the first word of the chain
markov_chain = [start_word]

for i in range(num_of_words):

    # access the values from the latest word's key in the dict
    newest_word_choices = d[markov_chain[-1]]

    # add a new word to the chain by grabbing one of the possible values
    markov_chain.append(np.random.choice(newest_word_choices))

print(' '.join(markov_chain))

# TODO: construct 5 random sentences

'''upon the kitten's fault entirely. 
For the chimney-piece while she could only the shovel--and here as the window 
all in the White Knight is sliding down on her knee, pretending to wind up, 
and hours getting to the window, and set him on the King took an enormous 
memorandum-book out to go the day came. Or--let me laugh so wide open: and 
grinned at her. So Alice was certain, that you're a grand game of it'''

'''that she could find one. "Blew--me--up," panted out, 
"My precious Lily! My imperial kitten!" and she could only pretence, 
just to be all her sister only get blown up!" 
Alice watched the leaves are something began winding up very pretty!" 
cried out, "My precious Lily! My imperial kitten!" and so, while she added, 
looking over outside. I shouldn't mind that was so tidy enough!" 
she added, as if some time to the pencil for Wednesday week--Suppose'''