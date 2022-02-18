grade = int(input("Enter Grade:"))

# if with single statement (indention)
if grade >= 70 and grade <= 100:
    print("Passed")
elif grade > 100 or grade < 0:
    print("Invalid")
else:
    print("Failed")
