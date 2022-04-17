input_number = int(input())
students_name_and_grades = {}
for _ in range(input_number):
    name, grade = tuple(input().split())
    if name in students_name_and_grades:
        students_name_and_grades[name].append(float(grade))
    else:
        students_name_and_grades[name] = [float(grade)]
for name, grades in students_name_and_grades.items():
    print(f"{name} -> {' '.join(format(x, '.2f' ) for x in grades)} (avg: {(sum(grades)/len(grades)):.2f})")