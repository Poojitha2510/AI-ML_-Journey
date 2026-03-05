#program to calulate the how many small letters in the given string
str = input("Enter a string:")
count=0
for i in str:
    if (ord(i) in range(97,123)):#i.isLower():
        count = count + 1
print("total small letters are are:",count)

# program to find the sum of all even digits in the given number
num=int(input("Enter a number:"))
num1=str(num)
sum=0
for i in num1:
    if int(i)%2==0:
        sum=sum+int(i)
print("Sum of all even digits in the given number is:",sum)

#program to find either the given string is palindrom or not
str=input("Enter a string:")
rev_str=str[::-1]
if str==rev_str:
    print("the given string is the palindrome")
else:
    print("the given string is not palindrome")