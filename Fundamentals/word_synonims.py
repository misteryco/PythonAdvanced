input_words = int(input())
synonym_dict = {}

for word in range(input_words):
    key = input()
    value = input()
    if key not in synonym_dict:
        synonym_dict[key] = []
    synonym_dict[key].append(value) # mnogo hitro ot Ines !!!!

for key in synonym_dict:
    print(f"{key} - {', '.join(synonym_dict[key])}")