def abs_value(number):
    if number < 0:
        number = -1 * number
    return number


numbers = [float(x) for x in input().split()]
result = [abs(n) for n in numbers]
print(result)
