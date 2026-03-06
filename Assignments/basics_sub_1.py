'''Write a Python program that simulates a simple Student Registration System.

Your program should:

Take student name as input.
Take student age as input.
Take mark1 as input
Take mark2 as input
Calculate total marks and average marks.
Display the following output:
Hello <name>
Age next year: <age+1>
Total Marks: <total>
Average Marks: <average>
Eligible for Scholarship: <True/False>
Scholarship Rule

A student is eligible if:

average marks greater than 75 AND
age less than 25
You must use:

Variables
Data types
Arithmetic operators
Logical operators
Expressions
input() and print()
'''

name=input("Enter your name:")
age=int(input("Enter your age"))
mark1=int(input("enter mark1:"))
mark2=int(input("enter mark2:"))
total=mark1+mark2
avg_marks=total/2
result=avg_marks>75 and age<25
print("Hello",name)
print("Age next year:",age+1)
print("Total Marks:",total)
print("Average Marks:",avg_marks)
print("Eligible for Scholarship:",result)
