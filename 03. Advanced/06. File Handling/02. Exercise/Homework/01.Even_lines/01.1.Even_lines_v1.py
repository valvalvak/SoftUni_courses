"""
Write a program that reads a text file and prints on the console its even lines.
Line numbers start from 0.
Before you print the result replace {"-", ",", ".", "!", "?"} with "@" and reverse the order of the words.
==========
Variant: 1
==========
"""

STRING_SET = {"-", ",", ".", "!", "?"}

with open("01_example.txt", "r") as file:
    for idx, row in enumerate(file):
        if idx % 2 == 0:
            for el in STRING_SET:
                row = row.replace(el, "@")
            words = reversed(row.split())
            print(" ".join(words))
