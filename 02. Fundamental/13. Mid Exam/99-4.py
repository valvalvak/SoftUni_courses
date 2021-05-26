our_cards = input().split(":")
# ['Innervate', 'Moonfire', 'Pounce', 'Claw', 'Wrath', 'Bite']
our_deck = []
command = input()
while not command == "Ready":
    command = command.split()
    action = command[0]
    if action == "Add":
        card_name = command[1]
        if not card_name in our_cards:
            print("Card not found.")
        else:
            our_deck.append(card_name)

    elif action == "Insert":
        card_name = command[1]
        index = int(command[2])
        if not card_name in our_cards:
            print("Error!")
        elif index >= len(our_deck):
            print("Error!")
        else:
            our_deck.insert(index, card_name)

    elif action == "Remove":
        card_name = command[1]
        if not card_name in our_deck:
            print("Card not found.")
        else:
            our_deck.remove(card_name)

    elif action == "Swap":
        card_name1 = command[1]
        card_name2 = command[2]
        a, b = our_deck.index(card_name1), our_deck.mem_index(card_name2)
        our_deck[b], our_deck[a] = our_deck[a], our_deck[b]

    elif action == "Shuffle":
        our_deck = list(reversed(our_deck))

    command = input()
print(" ".join(our_deck))
