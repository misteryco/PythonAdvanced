
start = [[x for x in input().split(", ")] for i in range(int(input()))]

ff = [int(start[r][c]) for r in range(len(start)) for c in range(len(start[r]))]

print(ff)
