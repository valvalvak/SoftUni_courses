def the_content_between_two_characters_according_to_ascii_table(cahr_a, cahr_b):
    result = ""
    cahr_a_as_int = ord(cahr_a)
    cahr_b_as_int = ord(cahr_b)
    for character in range(cahr_a_as_int + 1, cahr_b_as_int):
        result += chr(character) + " "
    return result


letter_a = input()
letter_b = input()

print(the_content_between_two_characters_according_to_ascii_table(letter_a, letter_b))
