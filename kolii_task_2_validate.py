def validate_division(x):
    while True:
        try:
            1/(33+x)
            return x
        except ZeroDivisionError:
            print('X value cause division by zero')
            x = int(input('Enter a new value for X: '))


def validate_input(var_name):
    while True:
        try:
            return int(input('{}:'.format(var_name)))
        except ValueError:
            print("Please, enter a NUMBER, retarded")
