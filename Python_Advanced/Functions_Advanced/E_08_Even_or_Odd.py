def even_odd(*args):
    if args[-1] == "even":
        return list(filter(lambda x: not x % 2, args[:len(args)-1]))
    else:
        return list(filter(lambda x: x % 2, args[:len(args)-1]))


print(even_odd(1, 2, 3, 4, 5, 6, "even"))
print(even_odd(1, 2, 3, 4, 5, 6, 7, 8, 9, 10, "odd"))
