import math

from kolii_task_3_validate import *

# Multi-paradigm languages: Task 3, Andrii Kolii FI-9119

print('Multi-paradigm languages: Task 3 \n Andrii Kolii FI-9119')

x = validate_input('X')
y = validate_input('Y')
x, y = validate_division(x, y)

result = (5 * x) / (x ** 3 + y ** 3) - 1 / math.tan((3 * x) / y)

print('Result: ', result)
