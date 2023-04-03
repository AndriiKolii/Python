def validate_division(comparison_function):
    while True:
        x = validate_input('x')
        if comparison_function(x):
            return x
        print('X value cause division by zero')


def validate_input(var_name):
    while True:
        try:
            return int(input('{}:'.format(var_name)))
        except ValueError:
            print('Please, enter a NUMBER, retarded')
