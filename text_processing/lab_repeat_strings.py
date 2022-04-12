list_of_strings = input().split()

for str in list_of_strings:
    print(str * len(str), end="")