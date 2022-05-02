main_strings = input().split("|")

final_strings_2 = [main_strings[idx].split() for idx in range(len(main_strings)-1, -1, -1)]

[print(' '.join(final_strings_2[row]), end=" ") for row in range(len(final_strings_2))]




# final_strings = []
# for idx in range(len(main_strings)-1, -1, -1):
#     final_strings.append(main_strings[idx].split())
# [print(' '.join(final_strings[row]), end=" ") for row in range(len(final_strings))]






