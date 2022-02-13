# Display student's marks from record

student_name = 'ralph'

student_marks = {'david': 90, 'ralph': 90, 'bill': 90}

for student in student_marks:
    if student == student_name:
        print(student_marks[student])
        break  # If there's no break, else statement executes.
else:
    print("No entry with that name found.")
