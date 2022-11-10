# Generate a matrix using the snake and snail methods.
# Transpose this matrix without using built-in function .transpose()


def checking_input_value(text):
    """The input value must be a number"""
    arg_num = input(f'Enter the number of {text}: ')
    try:
        int(arg_num)
        return int(arg_num)
    except ValueError:
        print('Invalid data. You must enter a number.')
        return checking_input_value(text)


def printing_matrix(matrix, size1, size2):
    """Prints the matrix element by element controlling width"""
    for i in range(size1):
        for j in range(size2):
            print(f'{matrix[i][j]:4d}', end='')  # 4 positions for each element
        print()


def fulling_matrix_snake(size1, size2):
    """Generate a matrix using the SNAKE method"""
    arg = 1
    matrix = [[0 for i in range(size2)] for j in range(size1)]

    for j in range(size2):
        if j % 2 == 0:
            for i in range(size1):
                matrix[i][j] = arg
                arg += 1
        if j % 2 == 1:
            for i in range(size1 - 1, -1, -1):
                matrix[i][j] = arg
                arg += 1
    return matrix


def fulling_matrix_snail(size1, size2):
    """Generate a matrix using the SNAIL method"""
    matrix = [[0 for i in range(size2)] for j in range(size1)]

    i = 0
    j = 0
    arg = 1

    while arg < size1 * size2:

        while matrix[i][j] == 0:
            matrix[i][j] = arg
            arg += 1
            j += 1
            if j == size2:
                break
        j -= 1
        i += 1

        while matrix[i][j] == 0:
            matrix[i][j] = arg
            arg += 1
            i += 1
            if i == size1:
                break
        i -= 1
        j -= 1

        while matrix[i][j] == 0:
            matrix[i][j] = arg
            arg += 1
            j -= 1
            if j == -1:
                break
        j += 1
        i -= 1

        while matrix[i][j] == 0:
            matrix[i][j] = arg
            arg += 1
            i -= 1
            if i == -1:
                break
        i += 1
        j += 1

    return matrix


def transposing_matrix(matrix, size1, size2):
    """Transpose the matrix"""
    tr_matrix = [[0 for x in range(size1)] for y in range(size2)]
    for i in range(size2):
        for j in range(size1):
            tr_matrix[i][j] = matrix[j][i]
    return tr_matrix


n = checking_input_value('rows')
m = checking_input_value('columns')

print('\nSnail:')
new_matrix = fulling_matrix_snail(n, m)
printing_matrix(new_matrix, n, m)

print('\nSnake:')
new_matrix = fulling_matrix_snake(n, m)
printing_matrix(new_matrix, n, m)

print('\nTranspose:')
new_matrix = transposing_matrix(new_matrix, n, m)
printing_matrix(new_matrix, m, n)
