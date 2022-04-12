shopping_list = input().split("!")
command = input()
# print(command)
while command != "Go Shopping!":
    command = command.split()
    if command[0] == "Urgent":
        item = command[1]
        if item not in shopping_list:
            shopping_list.insert(0, item)
    elif command[0] == "Unnecessary":
        item = command[1]
        if item in shopping_list:
            shopping_list.remove(item)
    elif command[0] == "Correct":
        old_item = command[1]
        new_item= command[2]
        for indx in range(len(shopping_list)):
            if shopping_list[indx] == old_item:
                shopping_list[indx] = new_item
    elif command[0] == "Rearrange":
        item = command[1]
        for indx in range(len(shopping_list)):
            if shopping_list[indx] == item:
                shopping_list.pop(indx)
                shopping_list.append(item)
    command = input()
print(", ".join(shopping_list))


