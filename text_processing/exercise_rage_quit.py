string = input()

letters_list = []
numbers_list = []
sub_string = ""

for idx in range(len(string)):

    if string[idx].isdigit():
        numbers_list.append(int(string[idx]))

    if not string[idx].isdigit():
        sub_string += string[idx].upper()
        if string[idx + 1].isdigit():
            letters_list.append(sub_string)
            sub_string = ""

total_list = [chr for x in letters_list for chr in x]
set_letters = set(total_list)

print(f"Unique symbols used: {len(set_letters)}")

for idx in range(len(letters_list)):
    print(f"{letters_list[idx]*numbers_list[idx]}", end ="")