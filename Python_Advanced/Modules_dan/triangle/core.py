def first_part(columns):
    for row in range(1, columns+1):
        for column in range(1, row+1):
            print(column, end=" ")
        print()


def second_part(columns):
    for row in range(columns, 0, -1):
        for column in range(1, row, 1):
            print(column, end=" ")
        print()


def print_triangular_columns(columns):
    first_part(columns)
    second_part(columns)
