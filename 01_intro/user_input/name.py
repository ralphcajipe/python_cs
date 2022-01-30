def say_hello(name):
    """Mentions input name with Hello."""
    print("\nHello", name)
    print("Welcome to Python 3 world!")


input_name = input("What's your name? ")
say_hello(input_name.title())
