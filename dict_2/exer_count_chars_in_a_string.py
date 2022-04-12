strings = input().split()
occurrences = {}
for substring in strings:
    for char in substring:
        current_char = char
        if current_char in occurrences:
            occurrences[current_char] += 1
        else:
            occurrences[current_char] = 1
for char, count in occurrences.items():
    print(f"{char} -> {count}")