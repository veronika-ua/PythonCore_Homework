# Use functions

def multiplication_table():
    for i in range(10):
        for ii in range(10):
            string = f'{ii + 1} x {i + 1} = {(ii + 1) * (i + 1)}'
            len_space = 13 - len(string)
            if ii == 9:
                print(string)
            else:
                print(string, ' ' * len_space, end='')


def checkerboard(checkerboard_size):
    for i in range(checkerboard_size):
        for ii in range(checkerboard_size):
            if i % 2 == ii % 2:
                if ii == checkerboard_size - 1:
                    print(chr(a))  # The next symbol will be from a new line
                else:
                    print(chr(a), end=' ')  # The next symbol will be on the same line
            else:
                if ii == checkerboard_size - 1:
                    print(chr(b))
                else:
                    print(chr(b), end=' ')


my_choose = input(f'Make a choice:\n1 - Display the checkerboard.\n2 - Display the multiplication table.\n')

if my_choose == '1':
    a = 9822  # Dark horse
    b = 9816  # Light horse
    checkerboard(10)
elif my_choose == '2':
    multiplication_table()
else:
    print('Invalid data. You must enter 1 or 2')
