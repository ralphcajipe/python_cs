def greet(name, message="Good morning!"):
    """Greets to the person with the message.
    If the message is not provided,
    it defaults to "Good morning!"
    """

    print(f"Hello {name}, {message}")


greet("Ralph")
greet("Ralph", "What's new?")