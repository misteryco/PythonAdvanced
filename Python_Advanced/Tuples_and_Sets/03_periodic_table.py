lines = int(input())
table = set()
for _ in range(lines):
    list_of_elements = input().split()
    [table.add(element) for element in list_of_elements]

[print(x) for x in table]



