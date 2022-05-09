file = open("numbers.txt", "r")
#  Var1 - reading the whole file split it and return a list
v1_list_of_data = list((int(number) for number in file.read().split()))
print(sum(v1_list_of_data))
# print(sum(v1_list_of_data))
#  Var 2 read line by line - type one
file = open("numbers.txt")
v2_list_of_data = [int(line[:-1]) for line in file.readlines() if len(line) > 1]
# print(v2_list_of_data)
print(sum(v2_list_of_data))
#  Var 3 read line by line type two
file = open("numbers.txt")
v3_list_of_data = 0
for line in file:
    v3_list_of_data += int(line)
print(v3_list_of_data)
#  Var 4 read line by line type two
# print([int(line) for line in open("numbers.txt")])
print(sum([int(line) for line in open("numbers.txt")]))
