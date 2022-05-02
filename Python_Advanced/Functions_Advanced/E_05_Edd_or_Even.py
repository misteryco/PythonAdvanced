def odd_or_even_sum(com, n):
    if com == 'Odd':
        odd = list(filter(lambda x: x % 2, n))
        # print(f"The sum of all odd numbers is: {' + '.join([str(x) for x in odd])} = {sum(odd)*len(numbers)}.")
        return sum(odd)
    else:
        even = list(filter(lambda x: not x % 2, n))
        # print(f"The sum of all even numbers is: {' - '.join([str(x) for x in even])} = {sum(even)*len(numbers)}.")
        return sum(even)


command = input()
numbers = [int(x) for x in input().split()]

print(f"{len(numbers)*odd_or_even_sum(command, numbers)}")