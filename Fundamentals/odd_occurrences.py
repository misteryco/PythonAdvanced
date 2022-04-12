words_list = [x.lower() for x in input().split()]
unique_words = {}

for inde in range(len(words_list)):
    if words_list[inde] in unique_words:
        unique_words[words_list[inde]] += 1
    else:
        unique_words[words_list[inde]] = 1

odd_list = []

for key in unique_words:
    if unique_words[key] % 2 != 0:
        odd_list.append(key)

print(f"{(' '.join(odd_list))}")
