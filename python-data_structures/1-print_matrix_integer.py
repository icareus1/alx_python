def print_matrix_integer(matrix=[[]]):
    for row in matrix:
        for num in row:
            print("{:d}".format(num))
            if not num[-1]:
                end = ' '
        print()