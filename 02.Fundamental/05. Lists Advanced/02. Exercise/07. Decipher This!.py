secret_message = input().split()
decipher = []
for n in range(len(secret_message)):
    word = secret_message[n]
    current_word = [el for el in word]
    digits_in_word = []
    for num in range(len(current_word)):
        if current_word[num].isdigit():
            digits_in_word.append(current_word[num])
    for digit in range(len(digits_in_word)):
        current_word.remove(digits_in_word[digit])
    digits_in_word = "".join(digits_in_word)
    digits_in_word = int(digits_in_word)
    current_word[0], current_word[-1] = current_word[-1], current_word[0]
    ascii_character = chr(digits_in_word)
    current_word.insert(0, ascii_character)
    current_word = "".join(current_word)
    decipher.append(current_word)
print(" ".join(decipher))
