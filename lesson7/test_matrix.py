from matrix import Matrix


if __name__ == '__main__':

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
