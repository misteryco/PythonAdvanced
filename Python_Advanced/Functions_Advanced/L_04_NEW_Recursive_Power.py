def recursive_power(n, power):
    if power == 0:
        return 1
    rec_p = recursive_power(n, power-1)
    return n * rec_p


print(recursive_power(2, 10))
print(recursive_power(10, 100))

#  below is shown solution with casual iteration

res = 1
n = 2
power = 10
for i in range(1, power+1):
    res *= n
print(res)
