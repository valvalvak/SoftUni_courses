"""
TASK:
#################################################
Write a program that reads a text file and inserts line numbers in front of each of its lines,
and counts all the letters and punctuation marks.
The result should be written to another text file.
#################################################
THE RESULT will be written in 02_result.txt in same directory
#################################################
"""
import re

letters = r"[A-Za-z]"  # to count all letters
punctuations = r"[^\w\s]"  # for underscore replace with r"([^\w\s]|_)"

result = []

with open("02_example.txt", "r") as example_file:
    for idx, line in enumerate(example_file):
        current_line_count = idx + 1
        letters_count = len(re.findall(letters, line))
        punctuations_count = len((re.findall(punctuations, line)))
        # line[:-1] to escape the new line command in the end of string("\n")" in current read line
        result.append([f"Line {current_line_count}: {line[:-1]} ({letters_count})({punctuations_count})\n"])

with open("02_result.txt", "w") as result_file:
    for line in result:
        result_file.write(*line)

######
# OR #
######
# for line in result:
#     with open("02_result.txt", "a") as result_file:
#         result_file.write(*line)

example_file.close()
result_file.close()
