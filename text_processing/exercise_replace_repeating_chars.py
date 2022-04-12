o_string = input()
opt_string = o_string[0]

for idx in range(1, len(o_string)):
    if o_string[idx-1] != o_string[idx]:
        opt_string += o_string[idx]
print(opt_string)