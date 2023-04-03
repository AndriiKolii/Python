from utils import validate_division, validate_input



# Multi-paradigm languages: Task 2, Andrii Kolii FI-9119
print('Multi-paradigm languages: Task 2 \n Andrii Kolii FI-9119')

x = validate_division(-33)
y = validate_input('Y')
z = validate_input('Z')

result = (15 + x / y) / (33 + x) - z
print('Result: ', result)
