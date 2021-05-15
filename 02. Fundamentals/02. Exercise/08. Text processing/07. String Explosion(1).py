text = input().split(">")
result = ""
memory = 0
for element in text:
    for character in element:
        if not character.isdigit():
            result += element
            break
        else:
            num = int(character)
            if num > len(element):
                memory += num - len(element)
                result += ">"
                break
            else:
                result += ">" + element[num + memory:]
                break
print(result)
