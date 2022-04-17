numbers = list(float(x) for x in input().split())
# print(numbers)
unique_numbers = set(numbers)
for number in unique_numbers:
    print(f"{number} - {numbers.count(number)} times")
