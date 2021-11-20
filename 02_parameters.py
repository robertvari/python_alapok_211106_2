# define a function
def say_hello(name):
    print(f"Hello {name}!")

# call function
#say_hello("Robert")


# multiple positional arguments
def say_hello2(name, age, address, email):
    print(f"Hello {name}! You are {age} old. You are from {address}. Email: {email}")


#say_hello2("tamas@gmail.com", "Tamás", 19, "Pécs")
# say_hello2(
#     address="Eger",
#     name="Kriszta",
#     age=20,
#     email="kriszta@gmail.com"
# )

# parameter annotation
def say_hello3(name: str, age: int, address: str, email: str):
    print(f"Hello {name}! You are {age} old. You are from {address}. Email: {email}")


# docstring
def say_hello4(name: str, age: int, address: str, email: str):
    '''
    This function prints out some data about a person
    :param name: Person name
    :param age: Person age
    :param address: Address
    :param email:  email
    :return: None
    '''
    print(f"Hello {name}! You are {age} old. You are from {address}. Email: {email}")


# default parameters
def say_hello5(name, age, address="Budapest", email="robert@gmail.com"):
    print(f"Hello {name}! You are {age} old. You are from {address}. Email: {email}")

# say_hello5("Tamás", 20)

# random length argument list
def say_hello6(*args):
    for i in args:
        print(i)

# say_hello6("Robert", 12345, 3.14, ["Alma", "körte", "szilve"])


# random length keyword argument list
def say_hello7(**kwargs):
    print(kwargs)

say_hello7(
    address="Eger",
    name="Kriszta",
    age=20,
    email="kriszta@gmail.com"
)