# The Emoji Printer

Terminals are awesome. They're happy places. Let's prove it: write a program that prints an emoji by name. This exercise is about practing dictionaries, so take the time to experiment and ask questions.

Example:
```
python3 emoji.py smiling

🙂
```
> In this example, when a user types in 'smiling' the program should output a smiling emoji.

**About Unicode**

Every language around the world has it's own alphabet. We encode those various alphabet into digital codes so that computers can transmit and print them accurately. [Unicode (UTF8 specifically)](https://en.wikipedia.org/wiki/Unicode) is 1 such standard of encoding characters.

Emoji codes are available as unicode characters. All you have to know is the code for the emoji you want to print and thats what you'll be using for this exercise.

**Instructions**

Using the emoji collection from the link below, add more emoji to the program and
test them out!

1. Gather a list of 10 of your favorite emoji codes from [Emojis v15](https://www.unicode.org/emoji/charts/full-emoji-list.html)
1. Experiment: try the unicode strings in the interpreter!
1. Write a function that returns an emoji by name (see examples).
1. OPTIONAL: See what happens if you just copy/paste an emoji from [Emojipedia](https://emojipedia.org/)


## Advanced 

Use the [`emoji.csv`]() file to create a new dictionary of more emoji! Use them in your program.

**Colorize**

You can also add more flare to terminal output with colors! Checkout the following color codes that you can use with strings.

```python
colors = {
    'header': '\033[95m',
    'blue': '\033[94m',
    'cyan': '\033[96m',
    'green': '\033[92m',
    'yellow': '\033[93m',
    'red': '\033[91m',
    'endc': '\033[0m',
    'bold': '\033[1m',
    'underline': '\033[4m'
}
```
