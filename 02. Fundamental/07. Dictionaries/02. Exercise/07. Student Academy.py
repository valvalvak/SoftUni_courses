n = int(input())
students_grades = {}

for i in range(n):
    student = input()
    grade = float(input())
    if student not in students_grades:
        students_grades[student] = [grade]
    else:
        students_grades[student] += [grade]
for name, grades in students_grades.items():
    average_grade = sum(grades) / len(grades)
    students_grades[name] = average_grade
for name, grades in sorted(students_grades.items(), key=lambda x: x[1], reverse=True):
    if grades >= 4.50:
        print(f"{name} -> {grades:.2f}")
