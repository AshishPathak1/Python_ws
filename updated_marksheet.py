from typing import Final
NUM_OF_SUBJECTS:Final[int] = 3
student_details = {}
for i in range (3):
    name = input("Enter Student's Name :")
    marks1 = int(input('Enter his marks in subject 1 :'))
    marks2 = int(input("Enter his marks in subject 2 :"))
    marks3 = int(input("Enter his marks in subject 3 :"))
    student_details[name] = {"subject1":marks1,"subject2":marks2,"subject3":marks3}
print("-"*80)
print(format(format("Mark sheet","*^20s"),"^80"))
print("-"*80)
print(f'{"Name":15.15s} {"subject1":<15s} {"subject2":<15s} {"subject3":<15s} {"Percentage ":<15s}')

for name in student_details :
    addition = (student_details[name]["subject1"] + student_details[name]["subject2"] + student_details[name]["subject3"])
    per = (addition / NUM_OF_SUBJECTS) 
    print(f'{name:15.15s} {student_details[name]["subject1"]:^15d} {student_details[name]["subject2"]:^15d} {student_details[name]["subject3"]:^15d} {per:>15.2f} % ')
print("-"*80)