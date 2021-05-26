def input_to_list(inputs):
    lines = []
    for _ in range(inputs):
        lines.append(input())
    return lines


def input_to_list_until_command(end_command):
    lines = []
    while True:
        command = input()
        if command == end_command:
            break
        lines.append(command)
    return lines


def is_vip_gust(guest):
    return guest[0].isdigit()


def separated_guests(guests):
    vip_guests = []
    regular_guests = []
    for guest in guests:
        if is_vip_gust(guest):
            vip_guests.append(guest)
        else:
            regular_guests.append(guest)
    return (sorted(vip_guests), sorted(regular_guests))


def print_result(guests):
    print(len(guests))
    (vip_guests, regular_guests) = separated_guests(guests)

    for guest in vip_guests:
        print(guest)
    for guest in regular_guests:
        print(guest)


# reservations = [
#     "7IK9Yo0h",
#     "9NoBUajQ",
#     "Ce8vwPmE",
#     "SVQXQCbc",
#     "tSzE5t0p",
# ]
# guests_arrived = [
#     "9NoBUajQ",
#     "Ce8vwPmE",
#     "SVQXQCbc",
#     "END",
# ]

guests_count = int(input())
reservations = input_to_list(guests_count)
guest_arrived = input_to_list_until_command("END")
guests_not_arrived = set(reservations) - set(guest_arrived)
print_result(guests_not_arrived)

# print(*(sorted (guests_not_arrived)))
