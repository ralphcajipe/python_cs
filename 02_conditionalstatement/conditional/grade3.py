grade = int(input("Enter Grade:"))
print("Passed") if grade >= 70 and grade <= 100 else print(
    "Invalid") if grade > 100 or grade < 0 else print("Failed")
