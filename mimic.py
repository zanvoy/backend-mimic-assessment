#!/usr/bin/env python
# -*- coding: utf-8 -*-

# Copyright 2010 Google Inc.
# Licensed under the Apache License, Version 2.0
# http://www.apache.org/licenses/LICENSE-2.0

# Google's Python Class
# http://code.google.com/edu/languages/google-python-class/

"""
Google's Python Class

Read in the file specified on the command line.
Do a simple split() on whitespace to obtain all the words in the file.
Rather than read the file line by line, it's easier to read
it into one giant string and split it once.

Build a "mimic" dict that maps each word that appears in the file
to a list of all the words that immediately follow that word in the file.
The list of words can be be in any order and should include
duplicates. So for example the key "and" might have the list
["then", "best", "then", "after", ...] listing
all the words which came after "and" in the text.
We'll say that the empty string "" is what comes before
the first word in the file.  This will be the seed string.

With the mimic dict, it's fairly easy to emit random
text that mimics the original. Print a word, then look
up what words might come next and pick one at random as
the next word.
Use the empty string as the first word to prime things.
If we ever get stuck with a word that is not in the dict,
go back to the empty string to keep things moving.

Note: the standard python module 'random' includes a
random.choice(list) method which picks a random element
from a non-empty list.

For fun, feed your program to itself as input.
Could work on getting it to put in linebreaks around 70
columns, so the output looks better.

"""

import random
import sys

__author__ = "Mike Gabbard"


def create_mimic_dict(filename):
    dict = {}
    with open(filename, 'r') as file:
        data = file.read()
        data = data.split(' ')
        dict[''] = [data[0]]
        dict[data[-1]] = ['']
        while len(data) > 1:
            if data[0] in dict:
                dict[data[0]].append(data[1])
            else:
                dict[data[0]] = [data[1]]
            data.pop(0)
    return dict


def print_mimic(mimic_dict, start_word):
    output = ''
    current_word = start_word
    for i in range(200):
        next_word = random.choice(mimic_dict[current_word])  
        output += ' ' + next_word
        current_word = next_word
    print(output)


def main():
    if len(sys.argv) != 2:
        print('usage: python mimic.py file-to-read')
        sys.exit(1)

    d = create_mimic_dict(sys.argv[1])
    print_mimic(d, '')


if __name__ == '__main__':
    main()
