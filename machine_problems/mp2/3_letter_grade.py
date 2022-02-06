letter_grade = input("Enter grade:")

if letter_grade == "A+":
    grade_pts = 4.0
elif letter_grade == "A":
    grade_pts = 4.0
elif letter_grade == "A-":
    grade_pts = 3.7
elif letter_grade == "B+":
    grade_pts = 3.3
elif letter_grade == "B":
    grade_pts = 3.0
elif letter_grade == "B-":
    grade_pts = 2.7
elif letter_grade == "C+":
    grade_pts = 2.3
elif letter_grade == "C":
    grade_pts = 2.0
elif letter_grade == "C-":
    grade_pts = 1.7
elif letter_grade == "D+":
    grade_pts = 1.3
elif letter_grade == "D":
    grade_pts = 1.0
elif letter_grade == "F":
    grade_pts = 0
else:
    print("Invalid grade entered.")

print(f"For this grade, you will receive a grade points of {grade_pts}")
