'''Write a Python program that performs the following tasks:

Take student name as input.
Take student marks (integer) as input.
Take attendance percentage as input.
Assign grade using conditionals:
Marks ≥ 90 → Grade A
Marks ≥ 75 → Grade B
Marks ≥ 50 → Grade C
Otherwise → Fail
Determine scholarship eligibility using nested conditionals:
Student must NOT fail.
Attendance must be greater than 80.
Display output in this format:

Hello name

Grade: grade

Scholarship Eligible: True/False'''
name=input("Enter your name: ")
marks=int(input("Enter your marks: "))
attend=int(input("Enter your attendence percentage: "))
print("Hello",name)
if(marks>=90):
    print("Grade: A")
elif(marks>=75):
    print("Grade: B")
elif(marks>=50):
    print("Grade: c")
else:
    print("Fail")
if(marks>=50):
    if(attend>80):
        value=True
    else:
        value=False
else:
    value=False
print("Scholarship Eligible: ",value)