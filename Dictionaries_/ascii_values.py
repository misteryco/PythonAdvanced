characters_list = input().split(", ")
char_dict = {char: ord(char) for char in characters_list}

# for char in characters_list:
#     char_dict[char] = ord(char)

print(char_dict)