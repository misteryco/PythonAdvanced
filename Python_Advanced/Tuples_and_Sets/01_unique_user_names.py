number_of_names = int(input())
users = set()

for _ in range(number_of_names):
    users.add(input())

[print(x) for x in users]

