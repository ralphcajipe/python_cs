grades = [50, 60, 70, 80, 90, 100]

for g in grades:
    if g >= 70 and g <= 100:
        print("Passed")
    else:
        print("Failed")
    # range(6) = range(0,6) 0,1,2,3,4,5
else:
    print("End of the first for statement")

for g in range(len(grades)):
    if grades[g] >= 70 and grades[g] <= 100:
        print("Passed")
    else:
        print("Failed")
