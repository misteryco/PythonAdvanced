def indexite(three_indexes_command):
    return int(three_indexes_command[1]), int(three_indexes_command[2])


given_list = list(map(lambda x: int(x),input().split()))
command = input()

while command != "end":
    command = command.split()
    current_command = command [0]
    if len(command) > 1:
        index_one, index_two = indexite(command)
    if current_command == "swap":
        given_list[index_one], given_list[index_two] = given_list[index_two], given_list[index_one]
    elif current_command == "multiply":
        given_list[index_one] = given_list[index_one] * given_list[index_two]
    elif current_command == "decrease":
        given_list = list(map(lambda x: x-1,given_list))
    command = input()
given_list = [str(x) for x in given_list]
print(", ".join(given_list))