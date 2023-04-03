from kolii_task_2_validate import *

# Multi-paradigm languages: Task 2, Andrii Kolii FI-9119

print('Multi-paradigm languages: Task 2 \n Andrii Kolii FI-9119')

x = validate_input('X')
x = validate_division(x)
y = validate_input('Y')
z = validate_input('Z')

result = (15 + x / y) / (33 + x) - z
print('Result: ', result)
