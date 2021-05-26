list_of_alms = input().split(", ")
number_of_beggars = int(input())

list_sums_of_alms_result = []
last_index = 0

for beggar in range(number_of_beggars):
    current_sum = 0
    for alms in range(last_index, len(list_of_alms), number_of_beggars):
        current_sum += int(list_of_alms[alms])
    last_index += 1
    list_sums_of_alms_result.append(current_sum)

print(list_sums_of_alms_result)
