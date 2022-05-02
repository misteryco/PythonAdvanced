def expression(num, current_res=0, current_expression=""):
    if len(num) == 0:
        print(f"{current_expression} = {current_res}")

        return
    expression(num[1:], current_res+num[0], f'{current_expression} +{num[0]}')
    expression(num[1:], current_res-num[0], f'{current_expression} -{num[0]}')


n = [int(x) for x in input().split()]
expression(n)
