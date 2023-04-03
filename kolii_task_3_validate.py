def validate_division(x, y):
    while True:
        try:
            1 / (x + y)
            return x, y
        except ZeroDivisionError:
            print('X and Y values cause division by zero')
            x = int(input('Enter a new value for X: '))
            y = int(input('Enter a new value for Y: '))


def validate_input(var_name):
    while True:
        try:
            return int(input('{}:'.format(var_name)))
        except ValueError:
            print("Please, enter a NUMBER, retarded")
