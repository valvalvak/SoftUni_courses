# def read_word():
#     result_as_list = [x for x in input().split(", ")]
#     return result_as_list
#
#
# def to_do_case():
#     raw_case = read_word()
#     solution_result = [f"{x} -> {len(x)}" for x in raw_case]
#     return solution_result
#
#
# print(*[x for x in to_do_case()], sep=", ")

words = input().split(', ')

result = [f"{word} -> {len(word)}" for word in words]

print(*result, sep="\n")
