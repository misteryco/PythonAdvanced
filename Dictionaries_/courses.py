command = input()
courses_info_dict = {}
while command != "end":
    command = command.split(" : ")
    current_course = command[0]
    current_student = command[1]
    if current_course not in courses_info_dict:
        courses_info_dict[current_course] = []
    courses_info_dict[current_course].append(current_student)
    command = input()

for cours, students in courses_info_dict.items():
    print(f"{cours}: {len(students)}")
    for student in students:
        print(f"-- {student}")

