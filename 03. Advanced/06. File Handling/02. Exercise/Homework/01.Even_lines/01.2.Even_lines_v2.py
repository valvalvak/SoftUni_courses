"""
Write a program that reads a text file and prints on the console its even lines.
Line numbers start from 0.
Before you print the result replace {"-", ",", ".", "!", "?"} with "@" and reverse the order of the words.
==========
Variant: 2
==========
"""
import re


def replace_symbol_regex(row):
    return re.sub(r"[-,.!?]", "@", row)  # works without escaping special characters when in []


with open("01_example.txt", "r") as file:
    for idx, row in enumerate(file):
        if idx % 2 == 0:
            """variant 1:"""
            # replaced_row = replace_symbol_regex(row).split()
            # print(" ".join(replaced_row[::-1]))
            """variant 2:"""
            replaced_row = " ".join(reversed(replace_symbol_regex(row).split()))
            print(replaced_row)

file.close()
