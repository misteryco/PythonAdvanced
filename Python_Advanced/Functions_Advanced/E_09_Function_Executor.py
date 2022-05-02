def sum_numbers(num1, num2):
    return num1 + num2


def multiply_numbers(num1, num2):
    return num1 * num2


def func_executor(*args):
    result = []
    for el in args:
        result.append(el[0](el[1][0], el[1][1]))  # we are giving arguments to function objects
    return result


print(func_executor((sum_numbers, (1, 2)), (multiply_numbers, (2, 4))))
