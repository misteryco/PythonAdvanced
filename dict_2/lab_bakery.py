string = input().split()
stock_dict = {}
for idx in range(len(string)):
    if idx %2 == 0 or idx == 0:
        stock_dict[string[idx]] = int(string[idx+1])
print(stock_dict)