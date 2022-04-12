usernames_list = input().split(", ")

for usrn in usernames_list:
    flag = False
    if not (3 <= len(usrn) <= 16):
        continue
    for char in usrn:
        if (not char.isalnum())or char == " ":
            flag = True
            if char == "-" or char == "_":
                flag = False
                continue
            break
    if flag:
        continue

    print(usrn)