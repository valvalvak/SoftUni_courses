def input_to_list(count):
    lines = list()
    for _ in range(count):
        lines.append(input())
    return lines


n = int(input())
students_grades_lines = input_to_list(n)

students_grades = {}


# n = int("7")
#
# students_grades_lines = (
#     'Peter 5.20',
#     'Mark 5.50',
#     'Peter 3.20',
#     'Mark 2.50',
#     'Alex 2.00',
#     'Mark 3.46',
#     'Alex 3.00'
# )

def avg_grade(grades):
    return sum(grades) / len(grades)


for line in students_grades_lines:
    students, grade = line.split()
    if students not in students_grades:
        students_grades[students] = float(grade),
    else:
        students_grades[students] += float(grade),

for (student, grades) in students_grades.items():
    student_grades_list = ' '.join(map(lambda grade: f"{grade:.2f}", grades))
    student_average_grade = avg_grade(grades)
    print(f"{student} -> {student_grades_list} (avg: {student_average_grade:.2f})")
