grade = int(input("Enter Grade:"))

# if with single statement (indention)
if grade >= 70 and grade <= 100:
    print("Passed")
    if grade > 90 and grade <= 100:
        print("Excellent")
    elif grade > 80 and grade <= 90:
        print("Very Satisfactory")
    else:
        print("Satisfactory")
elif grade > 100 or grade < 0:
    print("Invalid")
else:
    print("Failed")
