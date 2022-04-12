import math
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

    current_first_check_symbols = ""
    current_first_symbols = []
    first_part = ticket # triabva vichko tuk da stane ticket logikata s imenata e stara
    final_index = 0
    for idx in range(15):
        if idx >= final_index:
            current_char = first_part[idx]
            current_first_check_symbols = ""
            if current_char == "@" or current_char == "#" or current_char == "$" or current_char == "^":
                for check_idx in range(20):
                    if idx <= 15:
                        index = idx + check_idx
                        current_first_check_symbols += current_char
                        if (index + 1) == 20 or current_char != first_part[index + 1]:
                            if len(current_first_check_symbols) >= 6:
                                final_index = index + 1
                                current_first_symbols.append(current_first_check_symbols)
                            break

    counter_six = 0
    min_len = 20
    for element in current_first_symbols:
        if len(element) >= 6:
            counter_six += 1
        if len(element) < min_len:
            min_len = len(element)
    if len(current_first_symbols) >1:
        if min_len>= 6 and current_first_symbols[0][0] == current_first_symbols[1][0]:
            print(f'ticket "{ticket}" - {min_len}{current_first_symbols[0][0]}')
    elif len(current_first_symbols[0]) >= 12:
        if len(current_first_symbols[0]) == 20:
            print(f'ticket "{ticket}" - 10{current_first_symbols[0][0]} Jackpot!')
        else:
            min_len = int(math.floor(len(current_first_symbols[0]) / 2))
            print(f'ticket "{ticket}" - {min_len}{current_first_symbols[0][0]}')
    else:
        print(f"ticket '{ticket}' - no match")
