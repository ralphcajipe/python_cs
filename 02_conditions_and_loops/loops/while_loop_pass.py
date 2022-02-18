# while loop with the loop control `pass`
numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
i = 0
while i < len(numbers):
    print(i)
    i = i + 1
    if i == 5:
        pass
else:
    print("End of while loop.")
