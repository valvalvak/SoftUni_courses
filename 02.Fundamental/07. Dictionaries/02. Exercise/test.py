# command = input()
#
# result = {}
# pipe = " | "
# arrow = " -> "
# while not command == "Lumpawaroo":
#     if pipe in command:
#         side, user = command.split(pipe)
#         if side not in result:
#             result[side] = [user]
#         elif user not in result.values():
#             result[side].append(user)
#     elif arrow in command:
#         user, side = command.split(arrow)
#         if side not in result:
#             result[side] = [user]
#             print(f"{user} joins the {side} side!")
#         elif user not in list(x for x in result.values()):
#             result[side] = [user]
#             print(f"{user} joins the {side} side!")
#         else:
#             for key, value in result.items():
#                 if user in value:
#                     result[key].remove(user)
#             result[side].append(user)
#     command = input()
# sorted_result = dict(sorted(result.items(), key=lambda x: (len(x[1]), x[1]), reverse=True))
# for sides, users in sorted_result.items():
#     print(f"Side: {sides}, Members: {len(users)}")
#     for user in users:
#         print(f"! {user}")
