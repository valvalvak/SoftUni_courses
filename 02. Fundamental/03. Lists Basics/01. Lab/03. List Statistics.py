n = int(input())

positives = []
negatives = []

for _ in range(n):
    value = int(input())
    if value >= 0:
        positives.append(value)
    else:
        negatives.append(value)

print(positives)
print(negatives)
print(f"Count of positives: {len(positives)}. Sum of negatives: {sum(negatives)}")
