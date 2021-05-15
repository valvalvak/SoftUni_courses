dictionary_participants = {}

data = input()

while not data == "Lumpawaroo":
    try:
        if "|" in data:
            force_side, force_user = data.split(" | ")
            new_member = True
            for values in dictionary_participants.values():
                if force_user in values:
                    new_member = False
            if new_member:
                if force_side not in dictionary_participants:
                    dictionary_participants[force_side] = [force_user]
                else:
                    dictionary_participants[force_side].append(force_user)
        elif "->" in data:
            force_user, force_side = data.split(" -> ")
            if not force_side in dictionary_participants.keys():
                dictionary_participants[force_side] = [force_user]
                print(f"{force_user} joins the {force_side} side!")
            else:
                new_member = True
                pr = True
                for keys, values in dictionary_participants.items():
                    if force_user in values:
                        new_member = False
                        dictionary_participants[keys].remove(force_user)
                        dictionary_participants[force_side].append(force_user)
                        if keys == force_side:
                            pr = False

                if new_member:
                    dictionary_participants[force_side].append(force_user)
                    print(f"{force_user} joins the {force_side} side!")
                else:
                    if pr:
                        print(f"{force_user} joins the {force_side} side!")

    except:
        pass

    data = input()
else:
    # print(dictionary_participants)
    new_dictionary = dictionary_participants.copy()

    new_dictionary = dict(sorted(new_dictionary.items(), key=lambda x: (- len(x[1]), x[0])))

    for keys, values in new_dictionary.items():
        if not values == []:
            print(f"Side: {keys}, Members: {len(values)}")
            for mem in sorted(values):
                print(f"! {mem}")
