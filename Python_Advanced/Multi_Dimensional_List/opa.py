matrix_size = int(input())
r = 2
c = 10

for mini_row in range(3):
    for mini_col in range(3):
        r = rc - mini_row
        c = cc - mini_col
        if 0 <= r < matrix_size-1:
            if 0 <= c < matrix_size - 1:
                logic(r - 1, c + 1)