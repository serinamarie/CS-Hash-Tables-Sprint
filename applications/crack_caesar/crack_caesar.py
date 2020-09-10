# Use frequency analysis to find the key to ciphertext.txt, and then
# decode it.

# Unable to solve this one at the moment :/ 


def crack(filename):

    # open file
    with open(filename, 'r') as f:

        # set string text to variable
        string = f.read()

    # create an empty dict
    letter_dict = {}

    # for each character in our string
    for letter in string:

        # if character is a letter
        if letter.isalpha():
        
            # if letter not already in dict
            if letter not in letter_dict:

                # add new key/value pair
                letter_dict[letter] = 1
            
            # if letter in dict
            else:

                # increase count by 1
                letter_dict[letter] += 1

    # sort the letter frequencies
    letter_frequencies_sorted = sorted(letter_dict.items(), key=lambda x: (-x[1]))

    # create a caesar frequency list
    caesar_frequency_list = []

    for letter_desc in letter_dict.keys():
        caesar_frequency_list.append(letter_desc)

    real_world_frequencies = ['E', 'T', 'A', 'O', 'H', 'N', 'R', 'I', 'S', 'D', 'L', 'W', 'U', 'G', 'F', 'B', 'M', 'Y', 'C', 'P', 'K', 'V', 'Q', 'J', 'X', 'Z']


    # goal: replace current letters in string with real_world letters
    # we have caesar frequency list and real world frequency list, both in order
    # if a letter in string matches a letter in real world frequency list
        # find the real world frequency position (i) and replace it with the corresponding index in the caesar frequency list


    
        # find real world index
    
    for counter, value in enumerate(caesar_frequency_list):

            string = string.replace(letter, real_world_frequencies[counter])
    
    return string[:50]

    # ID EWKKF WDQSMDU ID JCW JIEW XB XSU
    # ET AOHHN
        # print(value, real_world_frequencies[counter])

        # for letter in string:
        #     # print(counter, value)
        #     # find index of letter within caesar freq
        #     if letter == value:
        #         print(letter, real_world_frequencies[counter])
        #         string = string.replace(letter, real_world_frequencies[counter])

  
                
     
        



        


    
    


if __name__ == '__main__':
    
    print(crack('ciphertext.txt'))