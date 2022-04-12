def between_symbols(stri, start_symbol, end_symbol):
    between = ""
    fl = False
    for idx in range(len(stri)):
        if fl:
            between += stri[idx]
        if stri[idx] == start_symbol:
            fl = True
        elif stri[idx+1] == end_symbol:
            break
    return between


lines = int(input())

for line in range(lines):
    strings = input()


    nam = between_symbols(strings, "@", "|")
    age = between_symbols(strings, "#", "*")

    print(f"{nam} is {age} years old.")
