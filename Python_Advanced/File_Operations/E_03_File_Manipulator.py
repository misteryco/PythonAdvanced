import os
command = input()
error_message = "An error occurred"

while command != "End":
    command = command.split("-")
    file_name = command[1]
    if command[0] == "Create":
        f = open(file_name, "w")
        f.close()
    elif command[0] == "Add":
        content = command[2] + '\n'
        f = open(file_name, "a")
        f.write(content)
        f.close()
    elif command[0] == "Replace":
        # try / except - error handling
        old_string = command[2]
        new_string = command[3]
        try:
            f = open(file_name, "r")
        except FileNotFoundError:
            print(error_message)
            command = input()
            continue
        current_content = f.read()
        f.close()
        new_content = current_content.replace(old_string, new_string)
        f = open(file_name, "w")
        f.write(new_content)
        f.close()
    elif command[0] == "Delete":
        # try / except - error handling
        try:
            os.remove(file_name)
        except FileNotFoundError:
            print(error_message)
            command = input()
            continue
    command = input()
