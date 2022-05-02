def operate(operator, *args):
    if operator == "+":
        res = 0
        for i in range(len(args)):
            res += args[i]
        return res
    elif operator == "-":
        res = 0
        for i in range(len(args)):
            res -= args[i]
        return res
    elif operator == "*":
        res = 1
        for i in range(len(args)):
            res *= args[i]
        return res
    elif operator == "/":
        res = 1
        for i in range(len(args)):
            res /= args[i]
        return res


print(operate("/", 1, 2, 3))

