words = [word for word in input().split()]
commands = input()

while not commands == "Stop":
    command = commands.split()
    cmd = command[0]

    if cmd == "Delete":
        index = int(command[1])
        if -1 <= index <= len(words) - 2:
            words.remove(words[index + 1])

    elif cmd == "Swap":
        word1 = command[1]
        word2 = command[2]
        if word1 in words and word2 in words:
            word1_index = words.index(word1)
            word2_index = words.index(word2)
            words[word1_index], words[word2_index] = words[word2_index], words[word1_index]

    elif cmd == "Put":
        index = int(command[2])
        word = command[1]
        if index == len(words) - 1:
            words.append(word)
        elif index - 1 in range(len(words)):
            words.insert(index - 1, word)

    elif cmd == "Sort":
        sorted_words = sorted(words, reverse=True)
        words = sorted_words

    elif cmd == "Replace":
        word_1 = command[1]
        word_2 = command[2]
        if word_2 in words:
            word_2_index = words.index(word_2)
            words[word_2_index] = word_1
    commands = input()

print(" ".join(words))
