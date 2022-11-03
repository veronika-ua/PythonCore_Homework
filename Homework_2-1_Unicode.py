# Enter the symbol code, using it to display the symbol itself on the screen.

while True:
    a = input('Enter the Unicode: ')
    try:
        int(a)
        break
    except ValueError:
        print('Invalid data. You must enter a number.')

print(chr(int(a)))
