
'''number =100
if number>90:
    print("first if")
print("out of if")'''

'''marks=95
if marks>90:
    print("Grade A")
if marks>80:
    print("Grade B")
if marks>70:
    print("Grade c")
else:
    print("Grade D")  // Grade A
Grade B
Grade D'''
 
"""if any condition if or elif condition true then it not check all"""
'''marks=95
if marks>90:
    print("Grade A")
elif marks>80:
    print("Grade B")
elif marks>70:
    print("Grade c")
else:
    print("Grade D")#Grade A'''

'''marks=94
if marks>=95:
    if marks>99:
        print("Topper")
    elif marks>=97 and marks<99:
        print("Second topper")
    elif marks>95:
        print("third topper")
    else:
        print("fourth topper")
elif marks>90:
    if marks>=93:
        if marks>=94:
            print("Almost close")# it will print 
        elif marks>=93:
            if marks==93:
                print("Lost by 2")
            else:
                print("Last")'''

'''age=20

if age>18:#it only cares true or false it not care about condition
    print("eligible for vote")
else:
    print("not eligible")
 
 #it only cares true or false it not care about condition

age=20
result=age>18
print(result)
if result:
    print("eligible for vote")
else:
    print("not eligible")


#if hardcoded to false then
age=10
result=age>18
print(result)
if result:
    print("eligible for vote")
else:
    print("not eligible")'''

#to check the given number is even or not
'''num=int(input("Enter a number"))
if(num%2==0):
    print("number is even")
else:
    print("number is odd")'''

#guess number

'''guess_number=56
num=int(input("enter the number"))
if(num==guess_number):
    print("you guess correct")
elif(num<guess_number):
    print("you guess lesser number,try a big number")
else:
    print("you guess the greter number,try with samller number")'''

 