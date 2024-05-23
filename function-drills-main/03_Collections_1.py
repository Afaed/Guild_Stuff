"""
Function Drills 03: Collections

This module will help you improve your understanding of functions and collections.
Collections are objects such as lists, dictionaries and tuples.

Instructions
------------

1. Read the description of each function.
2. Code your solution. All solutions are valid.
3. Pass all the tests!

To run the tests, simply execute this python script from the CLI.
Always solve 1 problem at a time.
"""
from __future__ import annotations


def sentence_count(text: str) -> int:
    """
    Given a block of text, return the total number of sentences in it.

    >>> sentence_count('A very. Bad sentence. Has taken. My Spirit.')
    4
    >>> sentence_count(BACK_TO_THE_FUTURE_1)
    4
    """
    # your code here


def shortest_words(text: str, amount: int) -> list:
    """
    Given a string of words, return the amount of shortest words.
    The string will not have any punctuation such as commas or apostrophes.

    Example usage:
    >>> shortest_words('i can count to five', 2)
    ['i', 'to']
    >>> shortest_words('green eggs taste amazing with salt', 3)
    ['eggs', 'with', 'salt']
    """
    # your code here


def word_space_analyzer(phrase: str) -> dict[str, int]:
    """
    Given a string, return a dictionary with a count of the 
    total words and the total spaces it contains.

    Example usage:
    >>> word_space_analyzer('monkeys like bananas')
    {'words': 3, 'spaces': 2}
    >>> word_space_analyzer(BACK_TO_THE_FUTURE_3)
    {'words': 94, 'spaces': 89}
    >>> word_space_analyzer(BACK_TO_THE_FUTURE_4)
    {'words': 160, 'spaces': 150}
    """
    # your code here


def find_duplicates(phrase: str) -> list:
    """
    Given a string, return a sorted list of words that appear more than once.

    Example usage:
    >>> find_duplicates('the box is in a box')
    ['box']
    >>> find_duplicates('the house has a room with a box with room for a box')
    ['a', 'box', 'room', 'with']
    """
    # your code here


def ordered_merge(list1: list, list2: list) -> list:
    """
    Given 2 lists of numbers, combine them into 1 and sort from lowest to highest.

    Example usage:
    >>> ordered_merge([3, 6, 9], [4, 8])
    [3, 4, 6, 8, 9]
    >>> ordered_merge([2, 4, 6], [1, 2, 3])
    [1, 2, 2, 3, 4, 6]
    """
    # your code here


def text_counter(text: str) -> dict[str, int]:
    """
    Return a dict with the count of each letter in a string. It will only
    contain alphanumeric characters. Do not record spaces or punctuation.

    Example usage:
    >>> text_counter('lovely eyes')
    {'l': 2, 'o': 1, 'v': 1, 'e': 3, 'y': 2, 's': 1}
    >>> text_counter('ghost in the shell')
    {'g': 1, 'h': 3, 'o': 1, 's': 2, 't': 2, 'i': 1, 'n': 1, 'e': 2, 'l': 2}
    """
    # your code here


# ==================================================================================
# Variables for testing. DO NOT EDIT.
# ==================================================================================


BACK_TO_THE_FUTURE_1 = """
This game is pretty simple. Your goal is to make your parents fall in love and go back to
1985. The photographs on the lower half of the screen are indicators of your progress; when you
get to complete the Marty McFly photo on the left, a piece of the right photograph will appear,
and the left one will go blank again. When you complete the right photo, your work will be done
and you can return.
"""

BACK_TO_THE_FUTURE_2 = """
As you play the game, you will hear two different tunes. When 'Johhny B Goode' plays,
you're losing ground, your mother is in love with you and the photos are disappearing. When 'The
Power of Love' plays, it's the opposite.
"""

BACK_TO_THE_FUTURE_3 = """There are five objects in the game. On the street, you can find the skate on the left end
and on the right end too. You will see the skate icon turn yellow at the top of the screen when
you are in front of it. Press the button and move up and you'll get it. With the skate, you can
move faster. The same goes for picking up the other objects. To use the object on a character,
wait until he/she touches you, then press the button while moving down to use it."""

BACK_TO_THE_FUTURE_4 = """
You will see the other four characters in the game. Biff goes around, knocking you
whenever he can. He's just in the game to make things a bit harder. Doc will be around too, as
well as your parents. Your mother will follow you around always; your father won't unless you
use the book on him. You'll find the book in the school library. Once you get him to follow you
as well as your mother, go to the 'Enchantment under the Sea' party and move over to the
instruments, where the guitar is. Use the guitar on your parents (use it on your mother *and*
your father too) and they will get stuck on the ground (with some luck, closely together). Move
away and if you've done everything right, the music will change and the photos will start to
reappear. After a minute or so, the effect of the guitar will vanish so you need to repeat the
process."""


if __name__ == '__main__':
    import doctest
    doctest.testmod()
