def nextPrimeList():
    num = eval(input(prompt))
    if num < 0:
        print("The number is not a positive integer")

    elif isinstance(num, float):
        print("The number should be whole value.")
    elif num > 0:
        def nextprime(n):
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
                nextprime(n)
                return

        nextprime(num)


prompt = "Enter a positive number:"
while True:
    nextPrimeList()
