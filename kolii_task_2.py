from utils import *


def validate_division():
    while True:
        x = validate_input('x')
        if x != -33:
            return x
        print('X value cause division by zero')


# Multi-paradigm languages: Task 2, Andrii Kolii FI-9119
print('Multi-paradigm languages: Task 2 \n Andrii Kolii FI-9119')

x = validate_division()
y = validate_input('Y')
z = validate_input('Z')

result = (15 + x / y) / (33 + x) - z
print('Result: ', result)
