def sum_of_between_numbers_with_recursion(start, end):
    if end == start:
        return end
    return sum_of_between_numbers(start, end-1) + end


def sum_of_between_numbers_with_loop(start, end):
    sum_ = 0
    for i in range(start, end+1):
        sum_ += i
    return sum_


print(sum_of_between_numbers_with_loop(-10000, 10))
print(sum_of_between_numbers_with_recursion(-600, 10))
