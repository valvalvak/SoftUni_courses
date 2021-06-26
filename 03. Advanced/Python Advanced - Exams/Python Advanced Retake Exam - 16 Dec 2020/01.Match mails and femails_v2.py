from collections import deque


def get_males_and_females_ques():
    """First you will be given a sequence of integers representing males.
    Afterwards you will be given another sequence of integers representing females."""
    stacks = [int(value) for value in input().split(" ")]
    return deque(stacks)


def special_case(female_value, male_value, females_que, males_que):
    if female_value % 25 == 0:
        if females_que:
            females_que.popleft()
        males_que.append(male_value)
    if male_value % 25 == 0:
        if males_que:
            males_que.pop()
        females_que.appendleft(female_value)
    return female_value, male_value, females_que, males_que


def main(females_candidates_que, males_candidates_que, matches_count):
    """You have to start from the first female and try to match it with the last male."""
    while True:
        if len(males_candidates_que) < 1 or len(females_candidates_que) < 1:
            return females_candidates_que, males_candidates_que, matches_count

        female_value = females_candidates_que.popleft()
        male_value = males_candidates_que.pop()

        if (female_value <= 0) and (0 < male_value):
            males_candidates_que.append(male_value)
            continue

        elif (male_value <= 0) and (0 < female_value):
            females_candidates_que.appendleft(female_value)
            continue

        elif female_value % 25 == 0 or male_value % 25 == 0:
            _, _, females_candidates_que, males_candidates_que = special_case(
                female_value, male_value, females_candidates_que, males_candidates_que
            )
            continue

        elif not male_value == female_value:
            male_value -= 2
            males_candidates_que.append(male_value)

        else:
            matches_count += 1


def print_matches(females_que, males_que, matches_results):
    print(f'Matches: {matches_results}')
    if males_que:
        print(f"Males left: {', '.join(map(str, reversed(males_que)))}")
    else:
        print('Males left: none')
    if females_que:
        print(f"Females left: {', '.join(map(str, females_que))}")
    else:
        print('Females left: none')


males_candidates = get_males_and_females_ques()
females_candidates = get_males_and_females_ques()
MATCHES = 0
femles_left, males_left, matches = main(females_candidates, males_candidates, MATCHES)

if __name__ == '__main__':
    print_matches(femles_left, males_left, matches)
