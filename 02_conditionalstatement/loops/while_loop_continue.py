# while loop with the loop control `continue`

numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
i = 0
while i < len(numbers):
    i = i + 1
    if i == 5:
        continue  # Skips 5 in loop
    print(i)
else:
    print("End of while loop")
