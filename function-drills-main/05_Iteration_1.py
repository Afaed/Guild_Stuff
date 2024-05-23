"""
Function Drills 05: Iteration 1

This module will help you improve your understanding of iteration in Python.
Each function below contains a test in its docstring.

Instructions
------------

1. Read the description of each function.
2. Code your solution. All solutions are valid.
3. Pass all the tests!

To run the tests, simply execute this python script from the CLI.
Always solve 1 problem at a time.
"""


def remove_duplicates(items: list[str]) -> list:
    """
    Given a list of variable size, remove all duplicates and return the list.

    Examples:
    >>> remove_duplicates(['a', 'b', 'a', 'c', 'b', 'd', 'a'])
    ['c', 'd']
    """
    # your code here
    dictionary = {}
    lst = []
    for item in items:
        if item not in dictionary:
            dictionary[item] = 1
        else:
            dictionary[item]+=1
    
    for obj in dictionary:
        if dictionary[obj] == 1:
            lst.append(obj)
    
    return lst


def get_vowel_count(text: str) -> int:
    """
    Suppose you want to count all the vowels in a given word. Return the number of vowels
    found.

    Example usage:
    >>> get_vowel_count('mississippi')
    4
    >>> get_vowel_count('oranges')
    3
    >>> get_vowel_count('pineapple')
    4
    """
    # your code here
    vowels = "aeiou"
    count = 0
    for letter in text:
        if letter in vowels:
            count+=1
    return count

def alpha_len(phrase: str) -> int:
    """
    Implement the len() function ...with a twist.
    Return the total number of letters in a given string, but do not count whitespace.
    >>> alpha_len('mouse')
    5
    >>> alpha_len('cat and mouse')
    11
    """
    # your code here
    return len(phrase.replace(" ", ""))


def print_until(condition: bool, text: str) -> str:
    """
    Given a string of variable size, print it until the condition is met.
    """
    # your code here


def transform(items: list, factor: int) -> list:
    """
    Given a list of variable length, multiply each item within by a given number. 
    Return the results in a list.

    Example:
    >>> transform(['a', 'b', 'c', 7], 3)
    ['aaa', 'bbb', 'ccc', 21]
    """
    answer = []
    sol = None
    # your code here
    for item in items:
        answer.append(item * factor)
        #answer.append(sol)
    return answer


if __name__ == '__main__':
    import doctest
    doctest.testmod()
    