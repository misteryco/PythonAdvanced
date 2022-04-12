journal = input().split(", ")
# print(journal)
command = input()
while command != "Craft!":
    command = command.split(" - ")
    # print(command)
    current_command = command[0]
    # print(current_command)
    if current_command == "Collect":
        item = command[1]
        # print(item)
        if item not in journal:
            journal.append(item)
    elif current_command == "Drop":
        item = command[1]
        if item in journal:
           journal.remove(item)
    elif current_command == "Combine Items":
        items = command[1].split(":")
        old_item = items[0]
        new_item = items[1]
        if old_item in journal:
           for index in range(len(journal)):
               if journal[index] == old_item:
                   journal.insert((index+1), new_item)
    elif current_command == "Renew":
        item = command[1]
        # print(item)
        if item in journal:
            for index in range(len(journal)):
                if journal[index] == item:
                    journal.pop(index)
                    journal.append(item)
    command = input()
print(", ".join(journal))