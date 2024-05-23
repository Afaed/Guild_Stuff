"""
Function Drills 04: Dictionaries 1

This module will help you improve your understanding of dictionaries.
Each function below contains a test in its docstring.

Learn more about docstrings: https://docs.python.org/3/library/doctest.html

Instructions
------------

1. Read the description of each function.
2. Code your solution. All solutions are valid.
3. Pass all the tests!

To run the tests, execute this python script from the CLI.

Always solve 1 problem at a time.
"""
from __future__ import annotations

# This variable is used to test your solutions. Do not edit.
shuri = {'name': 'Shuri', 'location': 'Wakanda', 'title': 'Princess', 'job': 'Scientist'}


def get_attr(obj: dict, attr: str) -> str | None:
    """
    Given a dictionary, return the given attribute (attr). Return None
    if attr not found.
    >>> get_attr(shuri, 'location')
    'Wakanda'
    """
    # Code here


def change_attr(obj: dict, attr: str, new_value: str) -> dict:
    """
    Given a dictionary, change a given attribute (attr) to the new_value.
    Return the new value.

    >>> change_attr(shuri, 'title', 'Black Panther')
    {'name': 'Shuri', 'location': 'Wakanda', 'title': 'Black Panther', 'job': 'Scientist'}
    """
    # Code here


def add_attr(obj: dict, attr_tuple: tuple) -> dict:
    """
    Given a dictionary, add the given attribute (attr_tuple) and return the dict.

    >>> add_attr(shuri, ('email', 'shuri@example.com',))
    {'name': 'Shuri', 'location': 'Wakanda', 'title': 'Princess', 'job': 'Scientist', 'email': 'shuri@example.com'}
    """
    # code here


def remove_attr(obj: dict, attr: str) -> dict:
    """
    Given a dictionary, remove the given attribute (attr) and return the
    modified dict.

    >>> remove_attr(shuri, 'title')
    {'name': 'Shuri', 'location': 'Wakanda', 'job': 'Scientist'}
    >>> remove_attr(shuri, 'email')
    {'name': 'Shuri', 'location': 'Wakanda', 'title': 'Princess', 'job': 'Scientist'}
    """
    # code here


def get_keys(obj: dict) -> list:
    """
    Given a dictionary, return only the keys.

    >>> get_keys(shuri)
    ['name', 'location', 'title', 'job']
    """
    # code here


def get_values(obj: dict) -> list:
    """
    Given a dictionary, return only the values.

    >>> get_values(shuri)
    ['Shuri', 'Wakanda', 'Princess', 'Scientist']
    """
    # code here


def transform(obj: dict) -> list:
    """
    Given a dictionary, transform it by returning a list of two-tuples
    containing key, value pairs.

    >>> transform({ 'name': 'Shuri', 'location': 'Wakanda'})
    [('name', 'Shuri'), ('location', 'Wakanda')]
    """
    # code here


if __name__ == '__main__':
    import doctest
    doctest.testmod()
