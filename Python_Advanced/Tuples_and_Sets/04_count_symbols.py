string = input()
symbols_counter = {}
for symbol in string:
    if symbol in symbols_counter:
        symbols_counter[symbol] += 1
    else:
        symbols_counter[symbol] = 1
# order = sorted(symbols_counter)
# for symbol in order:
#     print(f"{symbol}: {symbols_counter[symbol]} time/s")
[print(f"{symbol}: {symbols_counter[symbol]} time/s")for symbol in sorted(symbols_counter)]
