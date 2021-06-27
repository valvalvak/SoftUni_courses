from collections import deque


def main(bomb_effects, bomb_casings, smoke_decoy_bombs=120, cherry_bombs=60, datura_bombs=40):
    smoke_count = 0
    cherry_count = 0
    datura_count = 0

    while bomb_effects or bomb_casings:

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

    return {
        "Bomb Effects": bomb_effects,
        "Bomb Casings": bomb_casings,
        "Cherry count": cherry_count,
        "Datura count": datura_count,
        "Smoke decoy count": smoke_count,
    }


def print_solution(results):
    if results["Datura count"] >= 3 and results["Cherry count"] >= 3 and results["Smoke decoy count"] >= 3:
        print("Bene! You have successfully filled the bomb pouch!")
    else:
        print("You don't have enough materials to fill the bomb pouch.")

    if results["Bomb Effects"]:
        print(f"Bomb Effects: ", end="")
        print(', '.join(map(str, results["Bomb Effects"])))

    else:
        print("Bomb Effects: empty")

    if results["Bomb Casings"]:
        print(f"Bomb Casings: ", end="")
        print(', '.join(map(str, results["Bomb Casings"])))

    else:
        print("Bomb Casings: empty")

    print(f"Cherry Bombs: {results['Cherry count']}")
    print(f"Datura Bombs: {results['Datura count']}")
    print(f"Smoke Decoy Bombs: {results['Smoke decoy count']}")


bomb_effects_queue = deque([int(el) for el in input().split(", ")])
bomb_casing_queue = deque([int(x) for x in input().split(", ")])
result = main(bomb_effects_queue, bomb_casing_queue)
print_solution(result)
