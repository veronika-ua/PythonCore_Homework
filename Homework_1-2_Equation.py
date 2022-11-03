# Solve the equation: a * x^2 + b * x + c = 0

def my_input(name):
    while True:
        x = input(name)
        try:
            return float(x)
        except ValueError:
            print('Invalid data. You must enter a number.')


def my_equation(a, b, c):
    # discriminant
    d = b ** 2 - 4 * a * c
    x1 = (- b + d ** 0.5) / (2 * a)
    x2 = (- b - d ** 0.5) / (2 * a)

    if d > 0:
        print("x = " + str(x1) + " або " + str(x2))
    elif d == 0:
        print("x = " + str(x1))
    else:
        print('The discriminant is less than zero, so the equation has no valid solutions.')


print('Solve the equation: a * x^2 + b * x + c = 0, where а <> 0')

while True:
    a1 = my_input('Enter the number a: ')
    if a1 != 0:
        break
    else:
        print('Invalid data. The number a cannot be zero.')

b1 = my_input('Enter the number b: ')
c1 = my_input('Enter the number c: ')
my_equation(a1, b1, c1)
