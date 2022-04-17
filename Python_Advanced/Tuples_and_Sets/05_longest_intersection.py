lines = int(input())

max_intersection = [0, 0]

for line in range(lines):
    a, b = input().split("-")

    a = [int(number) for number in a.split(",")]
    b = [int(number) for number in b.split(",")]

    interval_a = set([n for n in range(a[0], a[1]+1)])
    interval_b = set([n for n in range(b[0], b[1]+1)])

    intersection = interval_a.intersection(interval_b)

    if len(intersection) > max_intersection[0]:
        max_intersection = [len(intersection), list(intersection)]

print(f"Longest intersection is {max_intersection[1]} with length {max_intersection[0]}")
