input_data = input()
phonebook = {}
while "-" in input_data:
    input_data = input_data.split("-")
    name = input_data[0]
    phone = input_data[1]
    phonebook[name] = phone
    input_data = input()

searches = int(input_data)

for search_r in range(searches):
    serach = input()
    if serach in phonebook:
        print(f"{serach} -> {phonebook[serach]}")
    else:
        print(f"Contact {serach} does not exist.")