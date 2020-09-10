# Use frequency analysis to find the key to ciphertext.txt, and then
# decode it.

# Your code here

# open file
# sort it by frequency

def crack(filename):

    # open file
    with open(filename, 'r') as f:

        # set string text to variable
        string = f.read()

    # create an empty dict
    letter_dict = {}

    # for each character in our string
    for letter in string:

        # we only want letters
        if letter.isalpha():
        
            # if not already in dict
            if letter not in letter_dict:

                # add new key/value pair
                # where value is the frequency of the letter in the string
                # and the key is that letter
                letter_dict[letter] = string.count(letter)

    # sort the letter frequencies
    letter_frequencies_sorted = sorted(letter_dict.items(), key=lambda x: (-x[1]))
    

    for tup in letter_frequencies_sorted:
        for letter in tup[0]:
            

            


    #     if letter.isalpha():
    #         letter.map()
    # return letter_frequencies_sorted



print(crack('ciphertext.txt'))