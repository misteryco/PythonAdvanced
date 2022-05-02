def concatenate(*args, res=""):
    for el in args:
        res += el
    return res


print(concatenate("Soft", "Uni", "Is", "Great", "!"))


