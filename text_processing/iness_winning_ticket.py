wining_chars = ['@', '#', '$','^']

def is_wining(t):
    if len(t) != 20:
        return "invalid ticket"
    left_half = ticket[:10]
    right_half = ticket[10:]
    for wining_char in wining_chars:
        for repet in range(10, 5, -1):
            char_repet = wining_char * repet
            if char_repet in left_half and char_repet in right_half:
                if repet == 10:
                    return f'ticket "{ticket}" - {repet}{wining_char} Jackpot!'
                elif 6 <= repet <= 9:
                    return f'ticket "{ticket}" - {repet}{wining_char}'
    return f'ticket "{ticket}" - no match'

tickets = [el.strip() for el in input().split(",")]
ticket_state = []
for ticket in tickets:
    ticket_state.append(is_wining(ticket))

for state in ticket_state:
    print(state)




