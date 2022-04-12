string = input()
chars_counter = {}

for char in string:
    if char != " ":
        if char not in chars_counter:
            chars_counter[char] = 0
        chars_counter[char] += 1

for char, count in chars_counter.items():
    print(f"{char} -> {count}")