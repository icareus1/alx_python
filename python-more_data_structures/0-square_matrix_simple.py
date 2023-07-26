def square_matrix_simple(matrix=[]):
    """This is a simpler version of it"""
    sq_matrix = []
    for row in matrix:
        sq_row = []
        for num in row:
            sq_row.append(num ** 2)
        sq_matrix.append(sq_row)
    return sq_matrix

# def square_matrix_simple(matrix=[]):
#     """Using lambda and map"""
#     sq_matrix = []
#     for row in matrix:
#         sq_row = list(map(lambda n: n ** 2, row))
#         sq_matrix.append(sq_row)
#     return sq_matrix