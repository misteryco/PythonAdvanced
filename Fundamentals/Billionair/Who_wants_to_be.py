from colorama import Fore, Style

questions = {"Кой е най-високият връх в българия" : "A",
             "Коя е морската столица на българия" : "B",
             "Коя река е най дългата гранична река на българия" : "A",
             "Какъв е Елон Мъск" : "A"}

answers = [["Мусала","София","Вихрен", "Витоша"],
           ["Марица","Варна","Пловдив","Лом"],
           ["Дунав","Перловска","Марица","Боянска"],
           ["Предриемач","Пехливанин","Просяк","Прелъстител"]]

questions_counter = 0
prize_money = [100, 500, 5000, 100000]
won_sum = 0
flag = False
print(f"")
print(f"{Fore.BLUE}Започваме играта с първи въпрос за 100 точки !{Style.RESET_ALL}")
print(f"{Fore.BLUE}--------------------------------------------------------{Style.RESET_ALL}")

for question, answer in questions.items():
    print(f"{Fore.GREEN}{question}{Style.RESET_ALL}")
    print(f"-----------------------------")
    answ_counter = 65
    for ans in answers[questions_counter]:
        print(f"{chr(answ_counter)}.{ans} ")
        answ_counter +=1
    print(f"-----------------------------")
    player_answer = input(f"{Fore.YELLOW}Въведете: А, B, C или D: {Style.RESET_ALL}").upper()
    print(f"Вие избрахте отговор: {player_answer}")
    while player_answer not in "ABCD":
        print(f"позволените отговори са : А, B, C или D: ")
        player_answer = input("Въведете: А, B, C или D: ").upper()
    if answer == player_answer:
        print(f"-----------------------------------------")
        print(f"Верен отговор - продължаваме със следващият въпрос за който е за {prize_money[questions_counter+1]} точки!")
        won_sum = prize_money[questions_counter]
    else:
        print(f"-----------------------------------------")
        print(f"Грешен отговор - играта приключи за вас !")
        flag = True
        break
    if flag:
        break
    questions_counter += 1
print(f"{Fore.RED}Вие спечелихте: {won_sum} точки")
