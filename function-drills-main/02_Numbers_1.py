"""
Function Drills 02: Numbers 1

This module will help you improve your understanding of functions and numbers.
Each function below contains a test in its docstring.

Learn more about docstrings: https://docs.python.org/3/library/doctest.html

Instructions
------------

1. Read the description of each function.
2. Code your solution. All solutions are valid.
3. Pass all the tests!

To run the tests, simply execute this python script from the CLI.
Always solve 1 problem at a time.
"""
from __future__ import annotations


def word_count(phrase: str) -> int:
    """
    Given a string, count the total number of words in it.

    Example usage:
    >>> word_count('monkeys like bananas')
    3
    """
    # your code here
    return len(phrase.split())


def is_odd(num: int) -> bool:
    """
    Given a number, return whether it's odd.

    Example usage:
    >>> is_odd(80)
    False
    >>> is_odd(543)
    True
    """
    # your code here
    if num % 2 == 0:
        return False
    else:
        return True


def modulo(dividend: int, divisor: int) -> int:
    """
    Given a dividend and a divisor, return the remainder of their division.

    Example usage:
    >>> modulo(7, 3)
    1
    """
    # your code here
    return dividend % divisor


def is_prime(num: int) -> bool:
    """
    Given a number, return true if it's a prime number, false if not.
    Learn more: https://byjus.com/maths/prime-numbers/

    Example usage:
    >>> is_prime(3)
    True
    >>> is_prime(10)
    False
    >>> is_prime(45)
    False
    """
    # your code here
    is_prime = True
    for i in range(2, num):
        if num % i == 0:
            is_prime = False
            break
    return is_prime

def get_highest(nums: str) -> int:
    """
    Given a string of numbers, return the highest number.

    Example usage:
    >>> get_highest('32 7 160 42')
    160
    """
    # your code here
    max_so_far = 0
    for n in nums.split():
        if int(n) > max_so_far:
            max_so_far = int(n)
    return max_so_far

def fibonacci_up_to(limit: int) -> int:
    """
    Given a number num, return a count of fibonacci numbers up to the limit.
    Example:
        fibonacci_count(10) means start the fibonacci sequence and continue up to 10.
        0, 1, 1, 2, 3, 5, 8 -> the next nubmer is 13, so you only the numbers up to 10.

        There are 7 fibonancci numbers up to 10

    HINT: https://byjus.com/maths/fibonacci-sequence/

    Example usage:
    >>> fibonacci_up_to(10)
    7
    >>> fibonacci_up_to(3)
    4
    """
    # your code here
    fib = 0
    counter = 0
    first = 0 
    second = 0
    for i in range(limit):
        
        counter += i
        
    return fib


def factorial(num: int) -> int:
    """
    Given a number, return its factorial.
    HINT: https://byjus.com/maths/factorial/

    Example usage:
    >>> factorial(3)
    6
    >>> factorial(5)
    120
    """
    # your code here


if __name__ == '__main__':
    import doctest
    doctest.testmod()
