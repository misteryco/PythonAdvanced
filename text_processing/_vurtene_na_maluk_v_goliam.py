aa = [0,1,2,3,4,5,6,7,8,9,10]
bb = ["a","b","c","d"]

for idx in range(len(aa)):
    if idx < len(bb):
        maluk_index = idx
    else:
        maluk_index = idx % len(bb)
    print(f"{aa[idx]} -> {bb[maluk_index]}")