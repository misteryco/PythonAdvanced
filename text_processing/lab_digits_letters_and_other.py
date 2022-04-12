input_string = input()
digits = ""
letters = ""
other = ""

for char in input_string:
    if char.isalpha():
        letters += char
    elif char.isnumeric():
        digits += char
    else:
        other += char

# out_list = ["".join(ch for ch in input_string if ch.isalpha()),
#             "".join(ch for ch in input_string if ch.isnumeric()),
#             "".join(ch for ch in input_string if (not ch.isnumeric() and not ch.isalpha()))]
#
# for _ in out_list:
#     print(_)

print(digits)
print(letters)
print(other)