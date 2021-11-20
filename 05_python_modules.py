#from utilities.math_functions import add_numbers, multiply_numbers, subdivide_numbers
from utilities import math_functions as MF
from simple_functions import say_hello

result = MF.add_numbers(4, 10)
result = MF.multiply_numbers(result, 10)
result = MF.subdivide_numbers(result, 2)
print(result)

say_hello("Robert")