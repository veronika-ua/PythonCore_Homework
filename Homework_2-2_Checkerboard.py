# Display the checkerboard.

while True:
    m = input('Enter the matrix size: ')
    try:
        n = int(m)
        break
    except ValueError:
        print('Invalid data. You must enter a number.')

a = 9822  # Dark horse
b = 9816  # Light horse

for i in range(n):
    for ii in range(n):
        if i % 2 == ii % 2:
            if ii == n - 1:
                print(chr(a))  # The next symbol will be from a new line
            else:
                print(chr(a), end=' ')  # The next symbol will be on the same line
        else:
            if ii == n - 1:
                print(chr(b))
            else:
                print(chr(b), end=' ')
