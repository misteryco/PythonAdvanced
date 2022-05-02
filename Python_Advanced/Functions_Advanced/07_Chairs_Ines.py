from itertools import combinations

combos = (list(combinations(input().split(", "), int(input()))))

for ind in range(len(combos)):
    print(*combos[ind], sep=", ")
