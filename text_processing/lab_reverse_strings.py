word = input()

while word != "end":
    print(f"{word} = {word[::-1]}")
    word = input()
    # res = ""
    # for idx in range((len(word)-1),-1,-1):
    #     res += word[idx]
    # print(f"{word} = {res}")
    #
    # word = input()