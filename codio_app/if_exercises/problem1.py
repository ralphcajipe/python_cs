# Write a python program that asks the user to input a length in
# centimeters. If the user enters a negative value, the program should tell
# the user that the entry is invalid. Otherwise, the program should convert
# the length to inches and print out the result. There are 2.54 centimeters
# in an inch.
user_input = input("Enter a length in centimeters: ")
cm = int(user_input)

if cm <= 0:
    print("Entry is invalid.")
else:
    inches = cm / 2.54
    print("Answer is: {} inches.".format(round(inches, 17)))
    # print("Answer is: %.17f inches " % inches)
    # print("Answer:", inch, "inches.")

# 14 decimals works
# 17 decimal works
