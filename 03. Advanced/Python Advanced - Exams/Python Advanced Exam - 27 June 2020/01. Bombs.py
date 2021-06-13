# from collections import dequeue

# def bomb_effect_dequeue(sequence):
#     queue_list_as_list = [int(el) for el in sequence.split(", ")]
#     return dequeue(queue_list_as_list)

# def bomb_casing_dequeue(sequence):
#     queue_list_as_list = [int(el) for el in sequence.split(", ")[::-1]]
#     return dequeue(queue_list_as_list)

# def combining_bombs_ques(effects, casing):
#     pass

# def main():
#     while True:
#         i = 0

#     if bomb_effects[i] + queue[i] == DATURA_BOMBS:
#         datura_count += 1
#         bomb_effects.popleft()
#         queue.pop(i)
#     elif bomb_effects[i] + queue[i] == CHERRY_BOMBS:
#         cherry_count += 1
#         bomb_effects.popleft()
#         queue.pop(i)
#     elif bomb_effects[i] + queue[i] == SMOKE_DECOY_BOMBS:
#         smoke_count += 1
#         bomb_effects.popleft()
#         queue.pop(i)
#     else:
#         queue[i] -= 5

#     if len(queue) < 1 or len(bomb_effects) < 1:
#         print("You don't have enough materials to fill the bomb pouch.")
#         break
#     if 2 < datura_count and 2 < cherry_count and 2 < smoke_count:
#         print("Bene! You have successfully filled the bomb pouch!")
#         break


# bomb_effects_queue  = bomb_effect_dequeue(input())
# bomb_casing_queue = bomb_casing_dequeue(input())

# DATURA_BOMBS = 40
# CHERRY_BOMBS = 60
# SMOKE_DECOY_BOMBS = 120

# cherry_count = 0
# datura_count = 0
# smoke_count = 0

# de = list(bomb_effects)

# if bomb_effects:
#     print(f"Bomb Effects: ", end="")
#     print(', '.join(map(str, de)))

# else:
#     print("Bomb Effects: empty")
# if queue:
#     print(f"Bomb Casings: ", end="")
#     print(', '.join(map(str, queue)))

# else:
#     print("Bomb Casings: empty")
# print(f"Cherry Bombs: {cherry_count}")
# print(f"Datura Bombs: {datura_count}")
# print(f"Smoke Decoy Bombs: {smoke_count}")