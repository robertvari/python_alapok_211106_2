def main(name):
    print("Hello. I'm the main function")

    def nested_function():
        print(f"Hello {name}")

    nested_function()

main("Robert")