# global scope
# global variable
name = "Tamás"


def say_may_name():
    # local scope
    # local variable
    name = "Robert"
    age = 20
    print(f"My name is {name}.")


def override_name(new_name):
    global name
    # override global name
    name = new_name


say_may_name()
override_name("Robert")
say_may_name()