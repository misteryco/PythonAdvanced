command = input()
languages_dict = {}
baned = {}
ban = False
while command != "exam finished":
    splitted_command = command.split("-")
    if len(splitted_command) == 3:
        user, language, points = splitted_command[0], splitted_command[1], int(splitted_command[2])
        if not language in languages_dict:
            languages_dict[language] = {user: [points]}
        else:
            copied_dict = languages_dict.copy()
            for lang, usr in copied_dict.items():
                if lang == language:
                    if user in copied_dict[lang]:
                        languages_dict[lang][user].append(points)
                    else:
                        languages_dict[lang][user] = [points]
    else:
        user_b = splitted_command[0]
        co_l_d = languages_dict.copy()
        for la, us in co_l_d.items():
            if user_b in co_l_d[la]:
                baned[la] = {user_b:languages_dict[la][user_b].copy()}
                del languages_dict[la][user_b]
                # else:
                #     baned[la][user_b] = languages_dict[la][user_b]
    command = input()

print(f"Results:")

for langu, users in languages_dict.items():
    for use, po in languages_dict[langu].items():
        print(f"{use} | {max(po)}")
print(f"Submissions:")
for langu, users in languages_dict.items():
    langu_subs = 0
    for use, po in languages_dict[langu].items():
        langu_subs += len(po)
    if langu in baned:
        for use, po in baned[langu].items():
            langu_subs += len(po)
    print(f"{langu} - {langu_subs}")

