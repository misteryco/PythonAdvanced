list_of_cards = input().split()

turn = input().split()
turn_counter = 0
flag_won = False
while turn[0] != "end":
    index_one = int(turn[0])
    index_two = int(turn[1])
    turn_counter += 1
    if (0 <= index_one < len(list_of_cards)) and (0 <= index_two < len(list_of_cards)):
            if index_one != index_two:
                if list_of_cards[index_one] == list_of_cards[index_two]:
                    print(f"Congrats! You have found matching elements - {list_of_cards[index_one]}!")
                    if index_two > index_one:
                        list_of_cards.pop(index_two)
                        list_of_cards.pop(index_one)
                        if len(list_of_cards) == 0:
                            flag_won = True
                            break
                    else:
                        list_of_cards.pop(index_one)
                        list_of_cards.pop(index_two)
                        if len(list_of_cards) == 0:
                            flag_won = True
                            break
                else:
                    print(f"Try again!")
    else:
        print(f"Invalid input! Adding additional elements to the board")
        middle = int(len(list_of_cards) / 2)
        list_of_cards.insert(middle, f"-{turn_counter}a")
        list_of_cards.insert(middle, f"-{turn_counter}a")
    turn = input().split()
if flag_won:
    print(f"You have won in {turn_counter} turns!")
else:
    print(f"Sorry you lose :(")
    print(" ".join(list_of_cards))







