from random import choice
import sys

def open_and_read_file(file_path):
    """Takes file path as string; returns text as string.

    Takes a string that is a file path, opens the file, and turns
    the file's contents as one string of text.
    """
    # body = ""
    # print type(file_path[0])
    contents = open(file_path[0]).read()
    contents = contents.split()
    # for item in contents:
    #     body += item + " "
    # print "body in open and read is ", body
    # return body.split()
    return contents

# print open_and_read_file("green-eggs.txt")

def make_chains(text_string):
    """Takes input text as string; returns _dictionary_ of markov chains.

    A chain will be a key that consists of a tuple of (word1, word2)
    and the value would be a list of the word(s) that follow those two
    words in the input text.

    For example:

        >>> make_chains("hi there mary hi there juanita")
        {('hi', 'there'): ['mary', 'juanita'], ('there', 'mary'): ['hi'], ('mary', 'hi': ['there']}
    """

    chains = {}
    for i in range(len(text_string)-2):
        # print i
        bigram = (text_string[i], text_string[i + 1])
        bigram_value = text_string[i + 2]
        # if bigram in chains.iterkeys():
        if bigram in chains.keys():
            chains[bigram].append(bigram_value)
        else:
            chains[bigram] = [bigram_value]
    # print "chains.keys() is ", chains.keys()
    return chains
# test_list = "this is a test this is not".split()
# print test_list
# print make_chains(test_list)

def make_text(chains):
    """Takes dictionary of markov chains; returns random text."""

    text = ""
    current_key = choice(chains.keys())
    text += current_key[0] + " " + current_key[1]

    # while current key does not raise a key error
    while True:
        try:
            value = choice(chains[current_key])
            text += " " + value
            new_key = (current_key[1], value)
            current_key = new_key
        except KeyError:
            break
    return text

input_path = sys.argv[1:]

# # # Open the file and turn it into one long string
input_text = open_and_read_file(input_path)

# # # Get a Markov chain
chains = make_chains(input_text)
# print chains.keys()
# # Produce random text
random_text = make_text(chains)

print random_text
