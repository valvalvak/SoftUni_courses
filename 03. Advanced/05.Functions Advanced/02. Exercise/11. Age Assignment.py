def age_assignment(*args, **kwargs):
    ages = {name: 0 for name in args}
    for first_letter, age in kwargs.items():
        for name in ages:
            if name.startswith(first_letter):
                ages[name] = age
    return ages


print(age_assignment("Peter", "George", G=26, P=19))
print(age_assignment("Amy", "Bill", "Willy", W=36, A=22, B=61))
