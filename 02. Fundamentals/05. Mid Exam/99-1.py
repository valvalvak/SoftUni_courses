def check_if_card_is_valid(item, list):
    if item in list:
        return True
    return False


cards = input().split(":")

action = input()

deck = []

while not action == "Ready":
    action = action.split()

    if action[0] == "Add":
        card = action[1]
        if check_if_card_is_valid(card, cards):
            deck.append(card)
        else:
            print(f"Card not found.")

    elif action[0] == "Insert":
        card = action[1]
        index = int(action[2])
        is_valid = False
        if index > len(deck) or card not in cards:
            print(f"Error!")
        else:
            deck.insert(index, card)

    elif action[0] == "Remove":
        card = action[1]
        if check_if_card_is_valid(card, deck):
            deck.remove(card)
        else:
            print(f"Card not found.")

    elif action[0] == "Swap":
        first_card = action[1]
        second_card = action[2]
        index_first_card = deck.index(first_card)
        index_second_card = deck.mem_index(second_card)
        deck[index_first_card], deck[index_second_card] = deck[index_second_card], deck[index_first_card]

    elif action[0] == "Shuffle":
        deck = [x for x in reversed(deck)]

    action = input()

if action == "Ready":
    print(" ".join(deck))