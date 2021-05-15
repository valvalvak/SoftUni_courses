capacity = int(input())
text = input()
info = {}
while not text == "Statistics":
    text = text.split("=")
    if text[0] == "Add":
        username = text[1]
        sent = int(text[2])
        received = int(text[3])
        if not username in info:
            info[username] = {"sent": sent, "received": received, "all":sent+received}
    elif text[0] == "Message":
        sender = text[1]
        receiver = text[2]
        if sender in info and receiver in info:
            if info[receiver]["received"] + 1 == 10:
                print(f"{receiver} reached the capacity!")
                info.pop(receiver)
                info[sender]["all"] += 1
                info[sender]["sent"] += 1
            if info[sender]["sent"] + 1 == 10:
                info[receiver]["received"] += 1
                info[receiver]["all"] += 1
                print(f"{sender} reached the capacity!")
                info.pop(sender)
            else:
                info[sender]["sent"] += 1
                info[sender]["all"] += 1
                info[receiver]["all"] += 1
                info[receiver]["received"] += 1
        elif receiver not in info:
            info[sender]["sent"] += 1
            info[sender]["all"] += 1
        elif sender not in info:
            info[receiver]["received"] += 1
            info[receiver]["all"] += 1
    elif text[0] == "Empty":
        user = text[1]
        if user == "All":
            info.clear()
        elif user in info:
            info.pop(user)
    text = input()

print(f"Users count: {len(info)}")
for user, stats in sorted(info.items(), key=lambda x: (-x[1]['received'], x)):
    print(f"{user} - {stats['all']}")
