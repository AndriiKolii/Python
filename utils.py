def validate_division(error_value):
    while True:
        x = validate_input('x')
        if x != error_value:
            return x
        print('X value cause division by zero')


def validate_input(var_name):
    while True:
        try:
            return int(input('{}:'.format(var_name)))
        except ValueError:
            print('Please, enter a NUMBER, retarded')
