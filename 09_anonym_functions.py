add_numbers = lambda a, b: a+b
multiply_numbers = lambda a, b: a*b
subdivide_numbers = lambda a, b: a/b


result = add_numbers(4, 10)
result = multiply_numbers(result, 10)
result = subdivide_numbers(result, 2)

print(result)