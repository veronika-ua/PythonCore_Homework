# Display the multiplication table

for i in range(10):
    for ii in range(10):
        string = f'{ii + 1} x {i + 1} = {(ii + 1) * (i + 1)}'
        len_space = 13 - len(string)
        if ii == 9:
            print(string)
        else:
            print(string, ' ' * len_space, end='')
