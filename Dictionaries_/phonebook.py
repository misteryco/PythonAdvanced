command = input()
phonebook = {}
while "-" in command:
    split_command = command.split("-")
    phonebook[split_command[0]] = split_command[1]
    command = input()
# print(phonebook)
search_count = int(command)
for _ in range(search_count):
    name = input()
    if name in phonebook:
        print(f"{name} -> {phonebook[name]}")
    else:
        print(f"Contact {name} does not exist.")
