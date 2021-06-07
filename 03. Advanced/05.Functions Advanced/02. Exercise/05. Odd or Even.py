def odd_solution(sequence, count):
    odds_nums_in_sequence = [int(x) for x in sequence if not x % 2 == 0]
    sum_odds = sum(odds_nums_in_sequence)
    return sum_odds * count


def even_solution(sequence, count):
    even_nums_in_sequence = [int(x) for x in sequence if x % 2 == 0]
    sum_evens = sum(even_nums_in_sequence)
    return sum_evens * count


odd_or_even_command = input()
sequence = [int(x) for x in input().split(" ")]
sequence_count = len(sequence)

if odd_or_even_command == "Odd":
    print(odd_solution(sequence, sequence_count))
elif odd_or_even_command == "Even":
    print(even_solution(sequence, sequence_count))
