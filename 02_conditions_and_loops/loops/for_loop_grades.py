grades = [80, 85, 90, 95, 100]
# index   0.  1.  2.  3.  4

for number in grades:
    print(number)
else:
    print("End of loop\n")

# range(5) is equivalent to 0-4
for number in range(len(grades)):
    if grades[number] == 90:
        break
    print(grades[number])
else:
    print("End of loop")
