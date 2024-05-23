"""
Function Drills 07: Lists 1

A function is a reusable unit of code. This module will help you improve your knowledge o Python.
Each function below contains a test in its docstring.

Learn more about lists: https://realpython.com/python-lists-tuples/

Instructions
------------

1. Read the description of each function.
2. Code your solution. All solutions are valid.
3. Pass all the tests!

To run the tests, simply execute this python script from the CLI.
Always solve 1 problem at a time.
"""


def get_second_item(items: list):
    """
    Return the second item in the items list.

    Example usage:
    >>> get_second_item(['apples', 'pears', 'peaches'])
    'pears'
    >>> get_second_item(['apples', 'peaches'])
    'peaches'
    """
    # your code here
    return items[1]


def get_last_item(items: list):
    """
    Return the last item in the items list.

    Example usage:
    >>> get_last_item(['apples', 'pears', 'peaches', 'cherries'])
    'cherries'
    >>> get_last_item(['bananas'])
    'bananas'
    """
    # your code here
    return items[-1]


def trim_first_and_last(items: list) -> list:
    """
    Return the list of items excluding the first and last item.

    Example usage:
    >>> trim_first_and_last(['shoes', 'shirt', 'belt', 'dress', 'slacks'])
    ['shirt', 'belt', 'dress']
    >>> trim_first_and_last(['shoes', 'shirt'])
    []
    >>> trim_first_and_last(['shoes'])
    []
    """
    # your code here
    items.pop(0)
    if items:
        items.pop(len(items) -1)
    return items


def remove_text(items: list, text: str) -> list:
    """
    Remove all items from the list that start with the given text and return the modified list.

    Example usage:
    >>> remove_text(['apples', 'pears', 'peaches', 'cherries'], 'p')
    ['apples', 'cherries']
    >>> remove_text(['shoes', 'shirt', 'belt', 'dress', 'slacks'], 'sh')
    ['belt', 'dress', 'slacks']
    >>> remove_text(['apples', 'pears', 'peaches', 'cherries'], 'd')
    ['apples', 'pears', 'peaches', 'cherries']
    """
    new = []
    # your code here
    for item in items:
        if item.find(text):
            new.append(item)
    return new


def get_first_items(items: list[list]) -> list:
    """
    Given a 2 dimensional list (a list of lists), return the first item from each list.

    Examples:
    >>> get_first_items([[1, 2, 3], [4, 5, 6], ['a', 'b', 'c']])
    [1, 4, 'a']
    """
    # your code here
    ans = []
    
    for item in items:
        ans.append(item[0])
    return ans

def find_first_number(items: list) -> int:
    """
    You have a list of items with lots of different strings and numbers in it.
    Return the first number you find in the list.

    Example usage:
    >>> find_first_number(['mangoes', 14, 'grapes', 8])
    14
    >>> find_first_number(['mangoes', '14', 'grapes', 8])
    8
    """
    # your code here
    ans = 0
    for item in items:
        if isinstance(item, int):
           return item


def get_longest_word(items: list) -> str:
    """
    Given a list of variable size, return the string with the most characters .

    Example usage:
    >>> get_longest_word(['street', 'bike', 'mountain', 'car'])
    'mountain'
    """
    # your code here
    
    big_string = ""

    for item in items:
        if len(item) > len(big_string):
            big_string = item

    return big_string

def find_duplicates(phrase: str) -> list:
    """Given a string, return a sorted list of words that are repeated.
    >>> find_duplicates('the box is in a box')
    ['box']
    >>> find_duplicates('the house has a room with a box with room for a box')
    ['a', 'box', 'room', 'with']
    """
    # your code here
    dictionary = {}
    lst = []
    
    for word in phrase.split():
        if word not in dictionary:
            dictionary[word] = 1
        else:
            dictionary[word]+=1
    
    for obj in dictionary:
        if dictionary[obj] > 1:
            lst.append(obj)
    lst.sort()
    return lst

def ordered_merge(list1: list[int], list2: list[int]) -> list:
    """
    Given 2 lists of numbers, combine them into 1 and sort from lowest to highest.
    
    >>> ordered_merge([3, 6, 9], [4, 8])
    [3, 4, 6, 8, 9]
    >>> ordered_merge([2, 4, 6], [1, 2, 3])
    [1, 2, 2, 3, 4, 6]
    """
    # your code here
    new = list1 + list2
    new.sort()

    return new

def flatten(items: list[list]) -> list:
    """
    Given a list of lists, flatten all lists into 1 list.

    Example:
    >>> flatten([[1, 2, 3], [4, 5, 6], ['a', 'b', 'c']])
    [1, 2, 3, 4, 5, 6, 'a', 'b', 'c']
    """
    # your code here
    flat = []

    for item in items:
        for sub in item:
            flat.append(sub)
    return flat


if __name__ == '__main__':
    import doctest
    doctest.testmod()
