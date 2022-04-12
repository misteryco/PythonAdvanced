force_user_dict = {}
command = input()
side_to_user = False
flag_two = False

while command != "Lumpawaroo":
    splitted_command = []
    if "|" in command:
        splitted_command = command.split(" | ")
        side_to_user = True
    if "->" in command:
        splitted_command = command.split(" -> ")
        side_to_user = False

    if side_to_user:
        f_side, f_user = splitted_command[0], splitted_command[1]
        if not f_side in force_user_dict:
            if len(force_user_dict) > 0:
                copy_of_dict = force_user_dict.copy()
                for val in copy_of_dict.values():
                    if f_user in val:
                        command = input()
                        continue
                    else:
                        force_user_dict[f_side] = [f_user]
            else:
                force_user_dict[f_side] = [f_user]
        else:
            copy1_of_dict = force_user_dict.copy()
            for val1 in copy1_of_dict.values():
                if f_user in val1:
                    command = input()
                    flag_two = True
                    continue
            if flag_two:
                continue
            force_user_dict[f_side] = [f_user]

    else:
        f_user, f_side = splitted_command[0], splitted_command[1]
        available_force_user = False
        available_force_side = False

        for key, value in force_user_dict.items():
            if f_user in value:
                available_force_user = True
                break

        if f_side in force_user_dict.keys():
            available_force_side = True

        if available_force_user and available_force_side:
            for key, value in force_user_dict.items():
                if f_user in value:
                    if len(force_user_dict[f_side]) > 0:
                        force_user_dict[f_side].append(f_user)
                        print(f"{f_user} joins the {f_side} side!")
                        force_user_dict[key].remove(f_user)
                        break
                    else:
                        force_user_dict[f_side] = [f_user]
                        print(f"{f_user} joins the {f_side} side!")
                        break
        if available_force_user and not available_force_side:
            for key, value in force_user_dict.items():
                if f_user in value:
                    force_user_dict[f_side] = [f_user]
                    print(f"{f_user} joins the {f_side} side!")
                    force_user_dict[key].remove(f_user)
                    break
        if not available_force_user and available_force_side:
            force_user_dict[f_side].append(f_user)
            print(f"{f_user} joins the {f_side} side!")
        if (not available_force_user) and (not available_force_side):
            force_user_dict[f_side] = [f_user]
            print(f"{f_user} joins the {f_side} side!")

    command = input()


for side, users in force_user_dict.items():
    if len(users) > 0:
        print(f"Side: {side}, Members: {len(users)}")
        for user in users:
            print(f"! {user}")