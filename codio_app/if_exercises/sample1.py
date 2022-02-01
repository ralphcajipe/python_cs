# Write a python program that inputs an integer from the user.
# Then your program should display a message indicating whether
# the integer is even or odd.
number = int(input("Please enter an integer: "))

if number % 2 == 0:
    print("This number is even.")
else:
    print("The number is odd.")
