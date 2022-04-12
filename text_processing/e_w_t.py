tickets = input().split(",")
flag = False
for ticket in tickets:
    ticket = ticket.strip()
    if len(ticket) != 20:
        print(f"invalid ticket")
        continue
    if "@" in ticket or "#" in ticket or "$" in ticket or "^" in ticket:
        flag = True
    if not flag:
        print(f'ticket "{ticket}" - no match')
        continue

    first_part = ticket[:10]
    second_part = ticket[10:]
    f_set = set(list(first_part))
    s_set = set(list(second_part))
    if len(f_set) == len(s_set) and len(f_set) == 1:
        if first_part[0] == second_part[0]:
            print(f'ticket "{ticket}" - 10$ Jackpot!')
            continue
        print(f"ticket {ticket} - no match")

    current_first_check_symbols = ""
    current_first_symbols = []
    for idx in range(5):
        current_char = first_part[idx]
        if len(current_first_check_symbols) >= 6:
            break
        current_second_check_symbols = ""
        if current_char == "@" or current_char == "#" or current_char == "$" or current_char == "^":
            for check_idx in range(9):
                if idx <= 4:
                    index = idx + check_idx
                    current_first_check_symbols += current_char
                    if (index + 1) == 10 or current_char != first_part[index + 1]:
                        current_first_symbols.append(current_first_check_symbols)
                        break


    current_second_check_symbols = ""
    current_second_symbols = []
    for idx in range(5):
        current_char = second_part[idx]
        if len(current_second_check_symbols) >= 6:
            break
        current_second_check_symbols = ""
        if current_char == "@" or current_char == "#" or current_char == "$" or current_char == "^":
            for check_idx in range(9):
                if idx <= 4:
                    index = idx + check_idx
                    current_second_check_symbols += current_char
                    if (index + 1) == 10 or current_char != second_part[index + 1]:
                        current_second_symbols.append(current_second_check_symbols)
                        break
    max_first = ""
    max_first_len = 0
    for string in current_first_symbols:
        if len(string) > max_first_len:
            max_first = string
            max_first_len = len(string)
    max_second = ""
    max_second_len = 0
    for string in current_second_symbols:
        if len(string) > max_second_len:
            max_second= string
            max_second_len = len(string)

    if max_first_len >= 6 and max_second_len >= 6 and max_first[0] == max_second[0]:
        print(f'ticket "{ticket}" - {min(max_first_len, max_second_len)}{max_first[0]}')
    else:
        print(f"ticket {ticket} - no match")


    # if len(current_first_symbols)>= 6 and len(current_second_symbols) >= 6 and current_first_symbols[0] == current_second_symbols[0]:
    #     print(f'ticket "{ticket}" - {min(len(current_first_symbols), len(current_second_symbols))}{current_first_symbols[0]}')