# Exchange values of two variables

def my_input(name):
    while True:
        x = input(name)
        try:
            return int(x)
        except ValueError:
            print('Invalid data. You must enter an integer.')


# ----------------- 1 -----------------
print('Method-1. Additional variable:')

print('Enter the numbers a and b:')
a = input()
b = input()

c = b
b = a
a = c

print('a = ', a)
print('b = ', b)


# ----------------- 2 -----------------
print('Method-2. Mathematical calculation:')

a = my_input('Enter the number a: ')
b = my_input('Enter the number b: ')

a += b
b = a - b
a -= b

print('a = ', a)
print('b = ', b)


# ----------------- 3 -----------------
print('Method-3. Cortege:')

print('Enter the numbers a and b:')
a = input()
b = input()

a, b = b, a

print('a = ', a)
print('b = ', b)
