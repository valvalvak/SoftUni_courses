def grade_data(grade_check):
    if 2.00 <= grade_check <= 2.99:
        return "Fail"
    elif 3.00 <= grade_check <= 3.49:
        return "Poor"
    elif 3.50 <= grade_check <= 4.49:
        return "Good"
    elif 4.50 <= grade_check <= 5.49:
        return "Very Good"
    elif 5.50 <= grade_check <= 6.00:
        return "Excellent"


grade = float(input())
result = grade_data(grade)
print(result)
