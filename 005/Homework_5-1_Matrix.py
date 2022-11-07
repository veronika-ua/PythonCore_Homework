# Create a random matrix. Find and wrote to the .txt file min and max elements.
# Swap the columns in the matrix with min and max elements.

import random


def input_num():
    """The input value must be a number"""
    while True:
        arg_num = input('Enter the matrix size: ')
        try:
            int(arg_num)
            return int(arg_num)
        except ValueError:
            print('Invalid data. You must enter a number.')


def text_width(arg_text, arg_width):
    """Adds spaces to the arg_text so that its length is arg_width"""
    len_space = arg_width - len(arg_text)
    return arg_text + ' ' * len_space


n = input_num()
max_list = [0, 0]   # list[0] is a max element, list[1] is a column index
min_list = [100, 0]   # list[0] is a min element, list[1] is a column index
random_matrix = [[0] * n for i in range(n)]  # create an empty matrix

for i in range(n):
    for ii in range(n):
        random_matrix[i][ii] = text_width(str(random.randint(1, 100)), 4)  # len(100) = 3 + '1 space' = 4
        print(random_matrix[i][ii], end='')
        if int(random_matrix[i][ii]) < min_list[0]:
            min_list[0] = int(random_matrix[i][ii])
            min_list[1] = ii

        if int(random_matrix[i][ii]) > max_list[0]:
            max_list[0] = int(random_matrix[i][ii])
            max_list[1] = ii
    print()

print('\nMin = ', min_list[0], ', column = ', min_list[1] + 1)
print('Max = ', max_list[0], ', column = ', max_list[1] + 1, '\n')

f = open("Homework_5-1_Matrix.txt", "w")
f.write(f'Min = {min_list[0]}\nMax = {max_list[0]}')
f.close()

for i in range(n):
    random_matrix[i][min_list[1]], random_matrix[i][max_list[1]] = \
        random_matrix[i][max_list[1]], random_matrix[i][min_list[1]]
    for ii in range(n):
        print(random_matrix[i][ii], end='')
    print()
