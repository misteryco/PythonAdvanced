def print_comb(txt, idx):
    if idx >= len(txt):
        print("".join(txt))
        return
    print_comb(txt, idx + 1)
    for i in range(idx+1, len(txt)):
        txt[idx], txt[i] = txt[i], txt[idx]
        print_comb(txt, idx + 1)
        txt[idx], txt[i] = txt[i], txt[idx]


the_text = list(input())
print_comb(the_text, 0)
