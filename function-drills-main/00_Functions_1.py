"""
Function Drills Intro

A function is a reusable unit of code. This module will help you improve your understanding of functions.
Each function below contains a test. 

Learn more about functions: https://realpython.com/lessons/functions-in-python/

Instructions
------------

1. Read the description of each function.
2. Code your solution. All solutions are valid.
3. Pass all the tests!

To run the tests, simply execute this python script from the CLI.
Always solve 1 problem at a time.
"""


def say_hello():
    """
    Look at this functions' signature. Return a string with the name of this function.

    Example usage:
    >>> say_hello()
    'say_hello'
    """
    # your code here


def say_hello_to(name):
    """
    Look at this functions' signature. Return the argument.
    HINT: https://realpython.com/defining-your-own-python-function/

    Example usage:
    >>> say_hello_to('Filip')
    'Filip'
    >>> say_hello_to('Kelsey')
    'Kelsey'
    """
    # your code here


def about_args(arg: str):
    """
    Look at this functions' signature. Return a string with the name of the data type of the argument.
    HINT: https://realpython.com/defining-your-own-python-function/

    Example usage:
    >>> about_args('This is a string.')
    'string'
    """
    # your code here


def about_return() -> str:
    """
    Look at this functions' signature. Return the name of the data type of the return value.
    HINT: https://realpython.com/defining-your-own-python-function/

    Example usage:
    >>> about_return()
    'string'
    """
    # your code here


if __name__ == '__main__':
    import doctest
    doctest.testmod()
    
