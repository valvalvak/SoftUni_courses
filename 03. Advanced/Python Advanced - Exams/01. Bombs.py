from collections import deque


def main(bomb_effects, bomb_casing, smoke_decoy_bombs=120, cherry_bombs=60, datura_bombs=40):
    smoke_count = 0
    cherry_count = 0
    datura_count = 0

    while bomb_effects or bomb_casing:

        if bomb_effects[0] + bomb_casing[0] == smoke_decoy_bombs:
            smoke_count += 1
            bomb_effects.popleft()
            bomb_casing.popleft()
        elif bomb_effects[0] + bomb_casing[0] == cherry_bombs:
            cherry_count += 1
            bomb_effects.popleft()
            bomb_casing.popleft()
        elif bomb_effects[0] + bomb_casing[0] == datura_bombs:
            datura_count += 1
            bomb_effects.popleft()
            bomb_casing.popleft()
        else:
            if not bomb_casing[0] - 5 < 0:
                bomb_casing[0] -= 5
            else:
                bomb_casing.popleft()

        if smoke_count >= 3 and cherry_count >= 3 and datura_count >= 3:
            break
        elif len(bomb_effects) < 1 or len(bomb_casing) < 1:
            break

    return {
        "Bomb effects": bomb_effects,
        "Bomb casing": bomb_casing,
        "Cherry count": cherry_count,
        "Datura count": datura_count,
        "Smoke decoy count": smoke_count,
    }


def print_solution(result):
    if result["Datura count"] >= 3 and result["Cherry count"] >= 3 and result["Smoke decoy count"] >= 3:
        print("Bene! You have successfully filled the bomb pouch!")
    else:
        print("You don't have enough materials to fill the bomb pouch.")

    if result["Bomb effects"]:
        print(f"Bomb Effects: ", end="")
        print(', '.join(map(str, result["Bomb effects"])))

    else:
        print("Bomb Effects: empty")

    if result["Bomb casing"]:
        print(f"Bomb Casings: ", end="")
        print(', '.join(map(str, result["Bomb casing"])))

    else:
        print("Bomb Casings: empty")

    print(f"Cherry Bombs: {result['Cherry count']}")
    print(f"Datura Bombs: {result['Datura count']}")
    print(f"Smoke Decoy Bombs: {result['Smoke decoy count']}")


bomb_effects_queue = deque([int(el) for el in input().split(", ")])
bomb_casing_queue = deque([int(x) for x in input().split(", ")][::-1])
result = main(bomb_effects_queue, bomb_casing_queue)
print_solution(result)
