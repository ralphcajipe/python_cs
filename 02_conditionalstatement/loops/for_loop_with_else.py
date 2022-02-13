numbers = [1, 3, 5, 11]

for num in numbers:
    if num % 2 == 0:
        print("The list contains an even number.")
        break
else:
    print("The list does not contain even number.")
