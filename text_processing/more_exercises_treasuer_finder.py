def between_symbols(stri, start_symbol, end_symbol):
    between = ""
    fl = False
    str_counter = 0
    for idx in range(len(stri)):
        if fl:
            between += stri[idx]
        if stri[idx] == start_symbol:
            str_counter += 1
            fl = True
        elif stri[idx+1] == end_symbol and str_counter == 1:
            break
    return between


key = input().split()
command = input()
decyphered = ""
while command != "find":
    decyphered = ""
    for idx in range(len(command)):
        if idx < len(key):
            small_index = idx
        else:
            small_index = idx % len(key)
        old_ord = ord(command[idx])
        decrese = int(key[small_index])
        new_ord = old_ord - decrese
        decyphered += chr(new_ord)
    # print(decyphered)
    typ = between_symbols(decyphered, "&", "&")
    coordinates = between_symbols(decyphered, "<", ">")
    print(f"Found {typ} at {coordinates}")
    command = input()