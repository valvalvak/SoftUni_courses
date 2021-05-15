cards = input().split()
number_of_faro_shuffles = int(input())


for shuffle in range(number_of_faro_shuffles):
    first_half = cards[:len(cards) // 2]
    second_half = cards[len(cards) // 2:]
    half_deck = len(first_half)
    temp_shuffle = []
    for index in range(half_deck):
        temp_shuffle.append(first_half[index])
        temp_shuffle.append(second_half[index])
    cards = temp_shuffle

print(cards)
