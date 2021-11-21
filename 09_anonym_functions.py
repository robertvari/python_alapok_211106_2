add_numbers = lambda a, b: a+b
multiply_numbers = lambda a, b: a*b
subdivide_numbers = lambda a, b: a/b


result = add_numbers(4, 10)
result = multiply_numbers(result, 10)
result = subdivide_numbers(result, 2)

name_list = ["Vári Róbert", "Kiss Elemér", "Nagy Adrienn", "Tóth Barna", "Kiss Elemér Aladár"]
number_list = [5, 2, 3, 7, 1, 87, 345, 987]

print(sorted(number_list))
print(sorted(name_list))

print(sorted(name_list, key=lambda name: name.split()[-1]))