number = int(input("Enter a number: "))
binary_digits = format(number, "b")

reversed_binary = binary_digits[::-1]
for binary in reversed_binary:
    print(binary)
