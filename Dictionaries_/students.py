command = input()
course_dict = {}
while ":" in command:
    command = command.split(":")
    name = command[0]
    identifier = command[1]
    course = command[2]
    if course not in course_dict:
        course_dict[course] = {}
    course_dict[course][identifier] = name
    command = input()

searched = command
if "_" in searched:
    searched = searched.replace("_", " ")

for course in course_dict:
    if course == searched:
        for key in course_dict[searched]:
            print(f"{course_dict[searched][key]} - {key}")
