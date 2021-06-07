def negatives(nums):
    negative_nums = [int(x) for x in nums if x < 0]
    return negative_nums


def positives(nums):
    positive_nums = [int(x) for x in nums if x >= 0]
    return positive_nums


nums = list(int(x) for x in input().split(" "))

negatives_sum = abs(sum(negatives(nums)))
positives_sum = sum(positives(nums))

print(sum(negatives(nums)))
print(sum(positives(nums)))

if negatives_sum > positives_sum:
    print("The negatives are stronger than the positives")
if positives_sum > negatives_sum:
    print("The positives are stronger than the negatives")
