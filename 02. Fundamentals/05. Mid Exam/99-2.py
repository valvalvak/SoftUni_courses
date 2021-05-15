friend_list = input().split(", ")
blacklist_counter = 0
lost_name_counter = 0
command = input()

while not command == "Report":
    command = command.split()
    if command[0] == "Blacklist":
        if command[1] in friend_list:
            print(f"{command[1]} was blacklisted.")
            blacklist_counter += 1
            index = friend_list.index(command[1])
            friend_list[index] = "Blacklisted"
        else:
            print(f"{command[1]} was not found.")
    if command[0] == "Error":
        index = int(command[1])
        if not friend_list[index] == "Blacklisted" and not friend_list[index] == "Lost":
            print(f"{friend_list[index]} was lost due to an error.")
            friend_list[index] = "Lost"
            lost_name_counter += 1
    if command[0] == "Change":
        index = int(command[1])
        if index in range(len(friend_list)):
            print(f"{friend_list[index]} changed his username to {command[2]}. ")
            friend_list[index] = command[2]
    command = input()
print(f"Blacklisted names: {blacklist_counter} \nLost names: {lost_name_counter} ")
print(f"{' '.join(friend_list)}")
