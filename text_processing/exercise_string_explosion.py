text = input()
power = 0
output = ''

for i in range(len(text)):
    if text[i] != '>' and power > 0:
        power -= 1
    elif text[i] == '>':
        power += int(text[i+1])
        output += text[i]
    else:
        output += text[i]

print(output)




# o_string = list(input())
#
# for idx in range(len(o_string)-1):
#     current_symbol = o_string[idx]
#     if o_string[idx] == ">":
#         strength = int(o_string[idx+1])
#         for explosion in range(idx+1, (idx+1 + strength)):
#             if explosion > len(o_string) - 1:
#                 break
#             if o_string[explosion] == ">":
#                 o_string[explosion] = ">!"
#                 strength += int(o_string[explosion + 1])+1
#         for explosion in range(idx+1, (idx+1 + strength)):
#             if explosion > len(o_string) - 1:
#                 break
#             if o_string[explosion] == ">!":
#                 continue
#             o_string[explosion] = "*"
#
# # print(o_string)
#
# new = "".join(o_string)
# # print(new)
# if "*" in new:
#     new = new.replace("*", "")
# if ">!" in new:
#     new = new.replace(">!", ">")
# print(new)