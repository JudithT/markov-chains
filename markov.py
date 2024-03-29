"""Generate Markov text from text files."""

from random import choice
from sys import argv


def open_and_read_file(file_path):
    """Take file path as string; return text as string.

    Takes a string that is a file path, opens the file, and turns
    the file's contents as one string of text.
    """


    contents = open(file_path).read()

    return contents


def make_chains(text_string):
    """Take input text as string; return dictionary of Markov chains.
    A chain will be a key that consists of a tuple of (word1, word2)
    and the value would be a list of the word(s) that follow those two
    words in the input text.

    For example:

        >>> chains = make_chains("hi there mary hi there juanita")

    Each bigram (except the last) will be a key in chains:

        >>> sorted(chains.keys())
        [('hi', 'there'), ('mary', 'hi'), ('there', 'mary')]

    Each item in chains is a list of all possible following words:

        >>> chains[('hi', 'there')]
        ['mary', 'juanita']
        
        >>> chains[('there','juanita')]
        [None]
    """
    #text_string = 

    chains = {}
    words = text_string.split()

    # your code goes here
    for i in range(len(words)-2):
        #lst = list()
        # print(i)
        key = (words[i], words[i+1])
        if key not in chains:
            chains[key] = chains.get(key,[])
        chains[key].append(words[i+2])
    
    return chains #chains



def make_text(chains):
    """Return text from chains."""

    key = choice(list(chains.keys()))
    words = [key[0],key[1]]

    # your code goes here
    
    while key in chains:
        random_choice = choice(chains[key])
        key = (key[1], random_choice)
        words.append(random_choice)

    return " ".join(words)


input_path = argv[1]

# Open the file and turn it into one long string
input_text = open_and_read_file(input_path)

# Get a Markov chain
chains = make_chains(input_text)

# Produce random text
random_text = make_text(chains)

print(random_text)
