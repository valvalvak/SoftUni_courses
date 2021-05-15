def solution(string, count):
    result = ""
    for _ in range(count):
        result += string
    return result
# Write a function that receives a string and a repeat count n.
# The function should return a new string (the old one repeated n times).


word = input()
rep = int(input())

print(solution(word, rep))
