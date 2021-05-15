def palindrome_check(test_list):
    result_list = []
    for a in range(len(test_list)):
        reversed_list = test_list[a][::-1]
        if test_list[a] == reversed_list:
            result_list.append("True")
        else:
            result_list.append("False")

    return result_list


input_list = input().split(", ")

result = (palindrome_check(input_list))

print(*result, sep="\n")
