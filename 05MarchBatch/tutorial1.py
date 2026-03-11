#if student name stars with vovel and age is greater than 10 he eligible for dance .if age less than 1o eligible for poem and name starts with consonent not eligible

name=input("Enter your name: ")
age=int(input("Enter your age:"))

ch=name[0]

if ch=="A" or ch=="E" or ch=="I" or ch=="O"or ch=="U" or ch=="a" or ch=="e" or ch=="i" or ch=="o" or ch=="u":
    if(age>10):
        print("Your are eligible for Dance")
    else:
        print("You are eligible for poem")
else:
    print("you are not eligible")