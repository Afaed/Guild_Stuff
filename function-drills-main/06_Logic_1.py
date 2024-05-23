"""
Function Drills 06: Logic 1

This module will help you understand basic programming logic. 

Supplemental Readings:
* https://realpython.com/python-conditional-statements/
* https://realpython.com/python-optional-arguments/
* https://realpython.com/python-kwargs-and-args

Instructions
------------

1. Read the description of each function.
2. Code your solution. All solutions are valid.
3. Pass all the tests!

To run the tests, simply execute this python script from the CLI.
Always solve 1 problem at a time.
"""


def is_legal_drinking_age(age: int, legal_age: int = 18) -> bool:
    """
    A young person wants to enter a night club and they're asked for their identification. Determine
    if they are the right age to enter or not.

    HINT: https://realpython.com/python-optional-arguments/

    Example usage:
    >>> is_legal_drinking_age(17)
    False
    >>> is_legal_drinking_age(84)
    True
    >>> is_legal_drinking_age(legal_age)
    True
    """
    # your code here


def is_sufficient_payment(payment: float, cost: float = 7.99) -> bool:
    """
    People are at the market shopping. As they find items they like, they use credits to buy them.
    When the credits are given to a merchant, they must determine if it's enough to cover the cost or not.

    Example usage:
    >>> is_sufficient_payment(6)
    False
    >>> is_sufficient_payment(8)
    True
    >>> is_sufficient_payment(7.50, 15.99)
    False
    """
    # your code here


def is_right_size(size: float, minimum: float = 2.15, maximum: float = 3.15) -> bool:
    """
    A tool shop makes widgets. Each order of widgets describes a size tolerance for each one.
    As each widget is checked, determine if it fits the size requirements or not.

    Example usage:
    >>> is_right_size(2.75)
    True
    >>> is_right_size(3.16)
    False
    >>> is_right_size(2.15)
    True
    >>> is_right_size(1.25, 0.75, 1)
    False
    """
    # your code here


def is_valid_user(username: str, password: str, valid_user: tuple = ('clementine', 's3cR3tZ')) -> bool:
    """
    A user wants to login to their account. Check that their username and password are correct.

    Example usage:
    >>> is_valid_user('rocky', 'balboa123')
    False
    >>> is_valid_user('clementine', 'balboa123')
    False
    >>> is_valid_user('clementine', 's3cR3tZ')
    True
    >>> is_valid_user('kathy_bates', 'biggestfan', ('kathy_bates', 'biggestfan',))
    True
    >>> is_valid_user('wutang', 'goatz', ('kathy_bates', 'biggestfan',))
    False
    """
    # your code here


def is_valid_email(email: str) -> bool:
    """
    Given an email address, check that it contains:
    - an '@' symbol after the first character
    - ends with '.com'.

    HINT: No interation/looping required.

    Example usage:
    >>> is_valid_email('rick@music.com')
    True
    >>> is_valid_email('@.com')
    False
    >>> is_valid_email('music.com@rick')
    False
    """
    # your code here



'''
BONUS CHALLENGE
===============
This is a map of a building. The 'P' represents the person entering the building, who you must 
give directions to. The persons left is the top of the map and the persons right is the bottom. 

To move through the building, they must go left, right or forwards as illustrated.
Each move advances the player to the end of a line, such that you always arrive at an intersection after a move.

LEFT
                      |_________
                      |
         _____________|
         |            |________ X
P _______             |                         --> FORWARD
         |____________|________                 <-- BACKWARD
                      |
                      |_________
                               |
                      _________|_________

RIGHT
'''


def is_correct_path(*directions) -> bool:
    """
    Using the map, guide the player to the location of the X by determining whether the directions
    provided are correct.
    - L means go left
    - R means go right
    - F means go forward
    HINT 1: No iteration/looping required.
    HINT 2: https://realpython.com/python-kwargs-and-args

    Example usage:
    >>> is_correct_path('L', 'F')
    False
    >>> is_correct_path('bagel')
    False
    >>> is_correct_path('F', 'L', 'F', 'L', 'F')
    False
    >>> is_correct_path('F', 'L', 'F', 'R', 'F')
    True
    >>> is_correct_path('F', 'L', 'F', 'L', 'R')
    False
    >>> is_correct_path('F', 'R', 'F', 'L', 'F')
    True
    """
    # your code here


if __name__ == '__main__':
    import doctest
    doctest.testmod()
