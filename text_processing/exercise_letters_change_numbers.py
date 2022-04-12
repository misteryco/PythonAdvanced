def number_in_alphabet(letter):
    return ord(letter.lower()) - (ord("a") - 1)

list_of_strings = input().split()
list_of_sums = []

for string in list_of_strings:

    front_letter = string[0]
    num = int(string[1:-1])
    end_letter = string[-1]
    f_number_in_alphabet = number_in_alphabet(front_letter)
    e_number_in_alphabet = number_in_alphabet(end_letter)
    if front_letter.isupper():
        num /= f_number_in_alphabet
    elif front_letter.islower():
        num *= f_number_in_alphabet
    if end_letter.isupper():
        num -= e_number_in_alphabet
    elif end_letter.islower():
        num += e_number_in_alphabet
    list_of_sums.append(num)

print(f"{sum(list_of_sums):.2f}")
