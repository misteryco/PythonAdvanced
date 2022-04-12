number_of_inputs = int(input())
student_grade_dict = {}
for _ in range(number_of_inputs):
    name = input()
    grade = float(input())
    if name not in student_grade_dict:
        student_grade_dict[name] = []
    student_grade_dict[name].append(grade)

for student in student_grade_dict.copy():
    average = sum(student_grade_dict[student]) / len(student_grade_dict[student])
    if average < 4.5:
        student_grade_dict.pop(student)
    else:
        print(f"{student} -> {average:.2f}")
# student_grade_dict = {st: gra for st, gra in student_grade_dict.items() if sum(student_grade_dict[st]) / len(student_grade_dict[st]) >= 4.5}
#
# for student in student_grade_dict.copy():
#     average = sum(student_grade_dict[student]) / len(student_grade_dict[student])
#     print(f"{student} -> {average:.2f}")