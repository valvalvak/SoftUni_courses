command = input()
results = {}
submissions = {}
banned = []
while not command == "exam finished":
    current_command = command.split("-")
    if "banned" not in current_command:
        username, language, points = current_command
        if username not in results:
            results[username] = int(points)
        else:
            if int(points) > int(results[username]):
                results[username] = int(points)
        if language not in submissions:
            submissions[language] = 1
        else:
            submissions[language] += 1
    else:
        username = current_command[0]
        banned.append(username)
        del results[username]
    command = input()

for user in banned:
    if user in results.keys():
        del results[user]

sorted_result = dict(sorted(results.items(), key=lambda x: (-x[1], x[0])))
sorted_submissions = dict(sorted(submissions.items(), key=lambda x: (-x[1], x[0])))
print("Results:")
for key, value in sorted_result.items():
    print(f"{key} | {value}")
print("Submissions:")
for key, value in sorted_submissions.items():
    print(f"{key} - {value}")
