book_list = input().split("&")
# print(book_list)
command = input()
while not command == "Done":
    command = command.split(" | ")
    if command[0] == "Add Book":
        if not command[1] in book_list:
            book_list.insert(0, command[1])
    elif command[0] == "Take Book":
        if command[1] in book_list:
            book_list.remove(command[1])
    elif command[0] == "Swap Books":
        left_book, right_book = command[1], command[2]
        if left_book in book_list and right_book in book_list:
            ind_l = book_list.index(left_book)
            ind_r = book_list.index(right_book)
            book_list[ind_l], book_list[ind_r] = book_list[ind_r], book_list[ind_l]
    elif command[0] == "Insert Book":
        book_list.append(command[1])
    elif command[0] == "Check Book":
        index = int(command[1])
        if index in range(len(book_list) - 1):
            print(book_list[index])
    command = input()
print(", ".join(book_list))
