# A student appears for at least 5 subjects in each semester
# Marks in every subject are out of 100
# Accept name and marks of 'n' number of students in two semesters
# Display the percentile marks of all students in both the semesters

import sys
from typing import Final
MAX_SCORE:Final[int]   = 100
MIN_NUMBER_OF_SUBJECTS = 5


total_students = input("Enter the number of students :")
if not total_students.isdigit() or int(total_students) < 0 :
    print("Enter valid Input",file=sys.stderr)
    sys.exit(0)
    
total_students = int(total_students)

student_details = {}

student_counter= 1
while student_counter<= total_students:
    print("Enter the details of student number : ", student_counter)
    name =  input("Enter the Student name :")
    number_of_subjects = input("How many subjects has the student appeared in Semester 1 : ")
    if not number_of_subjects.isdigit():
        print("Error: Specify number of subject in digits only",file=sys.stderr)
        print("Please enter the details of this student again")
        continue
    number_of_subjects = int(number_of_subjects)
    if number_of_subjects < MIN_NUMBER_OF_SUBJECTS:
        print("Error: Minimum number of Subjects is",MIN_NUMBER_OF_SUBJECTS,file=sys.stderr)
        print("Please enter the details of this student again")
        continue
    student_details[name] = {"sem1":[],"sem2":[]}
    sub_counter= 1
    while sub_counter<= number_of_subjects:
        marks = input( "Enter the marks in Subject Number " + str(sub_counter) + ": ")
        if not marks.isdigit():
            print("Error: Specify marks of subject in digits only",file=sys.stderr)
            print("Please enter the marks of this student again")
            continue
        marks = int(marks)
        if marks > MAX_SCORE:
            print("Error: Maximum score in any subject is",MAX_SCORE,file=sys.stderr)
            print("Please enter the marks of this student again")
            continue
        student_details[name]["sem1"].append(int(marks))      
        sub_counter= sub_counter+ 1
        
    number_of_subjects = input("How many subjects has the student appeared in Semester 2 : ")
    if not number_of_subjects.isdigit():
        print("Error: Specify number of subject in digits only",file=sys.stderr)
        print("Please enter the details of this student again")
        continue
    number_of_subjects = int(number_of_subjects)
    if number_of_subjects < MIN_NUMBER_OF_SUBJECTS:
        print("Error: Minimum number of Subjects is",MIN_NUMBER_OF_SUBJECTS,file=sys.stderr)
        print("Please enter the details of this student again")
        continue
    
    sub_counter= 1
    while sub_counter<= number_of_subjects:
        marks = input( "Enter the marks in Subject Number " + str(sub_counter) + ": ")
        if not marks.isdigit():
            print("Error: Specify marks of subject in digits only",file=sys.stderr)
            print("Please enter the marks of this student again")
            continue
        marks = int(marks)
        if marks > MAX_SCORE:
            print("Error: Maximum score in any subject is",MAX_SCORE,file=sys.stderr)
            print("Please enter the marks of this student again")
            continue
        student_details[name]["sem2"].append(int(marks))      
        sub_counter= sub_counter+ 1
  
    student_counter= student_counter+ 1   

print("Get the details of the Students")
while True:
    name = input("Please enter the student name: ")
    if name in student_details:
        print("Semester 1")
        marks = student_details[name]["sem1"]
        print("Marks     :", marks)
        print("Percentile:", sum(marks)/len(marks))
        print("Semester 2")
        marks = student_details[name]["sem2"]
        print("Marks     :", marks)
        print("Percentile:", sum(marks)/len(marks))
    else:
        print("Student not found!")
        
    wish = input("Do you want to fetch details of any more student(Y/N):")
    if wish.upper() not in ["YES",'Y']:
        break
