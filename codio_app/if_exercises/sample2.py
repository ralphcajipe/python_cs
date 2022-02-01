# Write a python program that inputs an integer from the user.
# Then your program should display a message mentioning the input
# and indicating whether the integer is even or odd.
number = int(input("Please enter an integer:"))

x = number % 2

if x == 0:
    print("The number", number, "is even...")
else:
    print("The number", number, "is odd...")
