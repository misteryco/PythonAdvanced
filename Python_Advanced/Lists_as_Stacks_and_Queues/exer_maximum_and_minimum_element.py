sequence = []
number_of_commands = int(input())
output = []
for _ in range(number_of_commands):
    command = input().split()
    this_command = command[0]
    if this_command == "1":
        number = int(command[1])
        sequence.append(number)
    elif this_command == "2":
        sequence.pop()
    elif this_command == "3":
        print(f"{max(sequence)}")
    elif this_command == "4":
        print(f"{min(sequence)}")

while sequence:
    output.append(str(sequence.pop()))
print(f"{', '.join(output)}")
# Dobawi prowerki za dyljina