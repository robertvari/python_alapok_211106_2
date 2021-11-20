def add_numbers(a, b):
    return a + b


def multiply_numbers(a, b):
    return a * b


def subdivide_numbers(a, b):
    return  a / b


result = add_numbers(4, 10)
result = multiply_numbers(result, 10)
result = subdivide_numbers(result, 2)

print(result)