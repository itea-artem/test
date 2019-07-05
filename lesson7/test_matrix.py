from matrix import Matrix


if __name__ == '__main__':

    # rows = [[0] * 5 for x in range(5)]
    # print(rows)
    #
    # rows[0][0] = 1
    # print(rows)

    n = m = 3
    matrix = Matrix(n, m)

    for i in range(0, n):
        matrix[i] = [5]*m

    matrix2 = Matrix(n, m)

    for i in range(0, n):
        matrix2[i] = [8] * m

    print(matrix)
    print(matrix2)
    print('sum:\n', matrix+matrix2)

    matrix.save()
    matrix2.save()