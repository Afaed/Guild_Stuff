import sys
from pathlib import Path
def descrable(user_text):
    with open('words.txt') as file:
        word_list = file.readlines()
        user = user_text
        tracker = 0
        answers = []
        for word in word_list:
            word = word.strip()
            if len(word) == len(user):
                for i in range(len(word)):
                    word_array = list(word)
                    if word_array[i] in user:
                        if word_array.count(word_array[i]) > 1:
                            for j in range(len(word_array)):
                                word_array.remove(word_array[i])
                        tracker += 1
                    else:
                        tracker = 0
                        break
            if tracker == len(user):
                tracker = 0
                answers.append(word)
        print(f"Possible Words: {answers}")

if __name__ == '__main__':
        descrable(sys.argv[1])