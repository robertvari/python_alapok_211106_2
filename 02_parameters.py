# define a function
def say_hello(name):
    print(f"Hello {name}!")

# call function
#say_hello("Robert")


# multiple positional arguments
def say_hello2(name, age, address, email):
    print(f"Hello {name}! You are {age} old. You are from {address}. Email: {email}")


say_hello2("tamas@gmail.com", "Tamás", 19, "Pécs")
say_hello2(
    address="Eger",
    name="Kriszta",
    age=20,
    email="kriszta@gmail.com"
)