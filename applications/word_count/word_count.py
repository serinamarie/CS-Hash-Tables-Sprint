def word_count(s):

    '''A function that takes in a string and returns a 
    dictionary of words and their counts'''

    # list of characters to ignore
    characters_to_ignore = ['"', ":", ";" , ".", "-", "+", "=", "/", "[", "]", "{", "}", "(", ")", ",", "*", "^", "&", "|", '\\']

    # for each character in input string
    for character in s:

        # if it's in the ignored characters
        if character in characters_to_ignore:

            # replace the value with whitepsace
            s = s.replace(character, ' ')

    # now, ready to make string a list by splitting string on whitespace
    words = s.split()

    # make all words in list lowercase
    words = [word.lower() for word in words]

    # create an empty dict
    word_dict = {}

    # for each word in our list of words 
    for word in words:

        # if not already in dict
        if word not in word_dict:

            # add new key/value pair
            word_dict[word] = words.count(word)

    return word_dict


if __name__ == "__main__":
    print(word_count(""))
    print(word_count("Hello"))
    print(word_count('Hello, my cat. And my cat doesn\'t say "hello" back.'))
    print(word_count('This is a test of the emergency broadcast network. This is only a test.'))
    

