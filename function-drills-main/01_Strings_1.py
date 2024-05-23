"""
Function Drills 01: Strings 1

This module will help you improve your understanding of functions and strings.
Each function below contains a test. 

Learn more about strings: https://docs.python.org/3/library/stdtypes.html#string-methods

Instructions
------------

1. Read the description of each function.
2. Code your solution. All solutions are valid.
3. Pass all the tests!

To run the tests, simply execute this python script from the CLI.
Always solve 1 problem at a time.
"""


def capitalize(word: str) -> str:
    """
    Capitalize a given word and return it.
    HINT: https://docs.python.org/3/library/stdtypes.html#str.capitalize

    Example usage:
    >>> capitalize('giraffe')
    'Giraffe'
    """
    # your code here
    return word.capitalize()

def lowercase(word: str) -> str:
    """
    Return a given word in all lowercase letters.
    HINT: https://docs.python.org/3/library/stdtypes.html#str.lower

    Example usage:
    >>> lowercase('CHIMPANZEE')
    'chimpanzee'
    >>> lowercase('AlliGatoR')
    'alligator'
    """
    # your code here
    return word.lower()

def uppercase(word: str) -> str:
    """
    Return a given word in all uppercase letters.
    HINT: https://docs.python.org/3/library/stdtypes.html#str.upper

    Example usage:
    >>> uppercase('crocodile')
    'CROCODILE'
    >>> uppercase('ElephaNt')
    'ELEPHANT'
    """
    # your code here
    return word.upper()

def first_last(word: str) -> str:
    """
    Return the first and last letter of a string.
    HINT: https://realpython.com/python-strings/

    Example usage:
    >>> first_last('turtle')
    'te'
    >>> first_last('peacock')
    'pk'
    """
    # Your code here
    return word[0] + word[-1]

def letter_swap(word1: str, word2: str) -> str:
    """
    Given two words, swap the first letter of each and return the new string.
    HINT: https://realpython.com/python-strings/#string-slicing

    Example usage:
    >>> letter_swap('mouse', 'cat')
    'couse mat'
    >>> letter_swap('koala', 'kangaroo')
    'koala kangaroo'
    >>> letter_swap('sloth', 'horse')
    'hloth sorse'
    """
    # Your code here
    
    return word1.replace(word1[0], word2[0]) + word2.replace(word2[0], word1[0])


def censor(word: str) -> str:
    """
    Take the first letter of a word and replace all occurrences thereafter with a '-'.
    Do not change the first letter of the word, only the following appearances.
    HINT: https://docs.python.org/3/library/stdtypes.html#str.replace

    Example usage:
    >>> censor('turtle')
    'tur-le'
    >>> censor('giggle')
    'gi--le'
    >>> censor('dragon')
    'dragon'
    """
    # Your code here 
    new = ""
    return word[0] + word[1:].replace(word[0], "-")

def flip(word: str) -> str:
    """
    Given a string, return it printed backwards.
    HINT: https://realpython.com/python-strings/#specifying-a-stride-in-a-string-slice
    
    Example usage:
    >>> flip('rhino')
    'onihr'
    >>> flip('red panda')
    'adnap der'
    """
    # your code here
    return word[::-1]
    


def shortest_word(text: str) -> str:
    """
    Given a string of words, return the shortest word.
    >>> shortest_word('i can count to five')
    'i'
    >>> shortest_word('green eggs taste amazing ')
    'eggs'
    """
    short = ""
    current = 10000000
    # your code here
    for word in text.split():
        length = len(word)
        if length < current:
            current = len(word)
            short = word

    return short

if __name__ == '__main__':
    import doctest
    doctest.testmod()
