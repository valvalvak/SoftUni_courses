from collections import deque


def are_bombs_pouches(bombs_pouches):
    return all([count >= 3 for count in bombs_pouches.values()])


def main(bomb_effects, bomb_casings, smoke_decoy_bombs=120, cherry_bombs=60, datura_bombs=40):
    smoke_count = 0
    cherry_count = 0
    datura_count = 0

    while bomb_effects and bomb_casings:

        bomb_effect = bomb_effects.popleft()
        bomb_casing = bomb_casings.pop()
        if bomb_effect + bomb_casing == smoke_decoy_bombs:
            smoke_count += 1
        elif bomb_effect + bomb_casing == cherry_bombs:
            cherry_count += 1
        elif bomb_effect + bomb_casing == datura_bombs:
            datura_count += 1
        else:
            if not bomb_casing - 5 < 0:
                bomb_casing -= 5
            bomb_effects.appendleft(bomb_effect)
            bomb_casings.append(bomb_casing)

        if smoke_count >= 3 and cherry_count >= 3 and datura_count >= 3:
            break
        elif len(bomb_effects) < 1 or len(bomb_casings) < 1:
            break
    bombs_ques = {
        "Bomb Effects": bomb_effects,
        "Bomb Casings": bomb_casings,
    }
    bombs_pouches = {
        "Cherry Bombs": cherry_count,
        "Datura Bombs": datura_count,
        "Smoke Decoy Bombs": smoke_count,
    }
    return bombs_ques, bombs_pouches


def print_solution(results):
    bombs_ques, bombs_pouches = results
    if not are_bombs_pouches(bombs_pouches):
        print("You don't have enough materials to fill the bomb pouch.")
    else:
        print("Bene! You have successfully filled the bomb pouch!")

    for bombs, ques in bombs_ques.items():
        if len(ques) > 0:
            print(f"{bombs}: {', '.join(map(str, ques))}")
        else:
            print(f"{bombs}: empty")
    for bombs, count in sorted(bombs_pouches.items()):
        print(f"{bombs}: {count}")


bomb_effects_queue = deque([int(el) for el in input().split(", ")])
bomb_casing_queue = deque([int(x) for x in input().split(", ")])
print_solution(main(bomb_effects_queue, bomb_casing_queue))
