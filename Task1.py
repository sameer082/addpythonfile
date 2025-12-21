"""
Creating a python code for dictionary of student marks and
asking user to give a name for knowing the marks of student...
"""

student_marks = {"Sameer": 85,"Deepak": 92,"Krishna": 78,"Rudra": 95}

student_name = input("Enter the student's name: ")


if student_name in student_marks:
    marks = student_marks[student_name]
    print(f"{student_name}'s marks: {marks}")
else:
    print("Sorry!! , Student not found..")