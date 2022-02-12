def nextPrimeList(n):
    """
    Will find and return the first prime number that is
    larger than some integer, n.
    """
    while True:
        if n < 0:
            print("The number is not a positive integer")
            n = eval(input(prompt_integer))
        elif isinstance(n, float):
            print("The number should be whole value.")
            n = eval(input(prompt_integer))

        elif n > 0:
            prime = 0
            n += 1
            for i in range(2, int(n ** 0.5) + 2):
                if n % i == 0:
                    prime = 0
                    break
                else:
                    prime = 1
            if prime == 1:
                print(
                    f"The first prime greater than the number entered is:{n}")
                return
            else:
                nextPrimeList(n)
                return


prompt_number = "Enter a positive number:"
prompt_integer = "Enter a positive integer:"
n = eval(input(prompt_number))
nextPrimeList(n)
