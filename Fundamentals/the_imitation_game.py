encrypted = [char for char in input()]

command = input()

while command != "Decode":
    command = command.split("|")
    current_command = command[0]
    if current_command == "Move":
        number_of_letters = int(command[1])
        if 0 <= number_of_letters <= len(encrypted):
            encrypted = encrypted[number_of_letters:] + encrypted[:number_of_letters]
    if current_command == "Insert":
        index = int(command[1])
        value = command[2]
        encrypted.insert(index, value)
    if current_command == "ChangeAll":
        substring = command[1]
        replacement = command[2]
        for indx in range(len(encrypted)):
            if encrypted[indx] == substring:
                encrypted[indx] = replacement
    command = input()

print(f"The decrypted message is: {''.join(encrypted)}")
