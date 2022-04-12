input_list = input().split()
min_len = min(len(input_list[0]), len(input_list[1]))
sum = 0

longer_string = input_list[0]
if len(input_list[0]) < len(input_list[1]):
    longer_string = input_list[1]

for idx in range(min_len):
    sum += ord(input_list[0][idx]) * ord(input_list[1][idx])

if len(input_list[0]) != len(input_list[1]):
    for idx in range(min_len, len(longer_string)):
        sum += ord(longer_string[idx])

print(sum)