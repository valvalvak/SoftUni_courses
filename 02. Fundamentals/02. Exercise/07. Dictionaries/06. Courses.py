command = input()
courses = {}
while not command == "end":
    course, student = command.split(" : ")
    if course not in courses:
        courses[course] = [student]
    else:
        courses[course] += [student]
    command = input()

for path, group in sorted(courses.items(), key=lambda x: len(x[1]), reverse=True):
    print(f"{path}: {len(group)}")
    group = sorted(group)
    for name in range(len(group)):
        print(f"-- {group[name]}")

