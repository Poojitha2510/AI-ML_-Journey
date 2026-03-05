'''a=10
b=20
print(a,b)'''
"""
Data types in python
1.int->whole number:without decimal point +ve,-ve,0
   ex:3,4,-10
   ->Infinite possible without a decimal point
2.float->Any number with a decimal point
  eg:3.14.3.0,2.77
  ->Infinite possible with a decimal point
3.string->anything written in singleor double quotes
  eg:"hello"
  ->Infinite possible which are enclosed in double quotes
4.boolean->yes/no:true or false
   ->only two possible values for booleans

print(type(variable_name))
"""
'''
a=10
print(type(a))#to know the type of variable
print(type("poojitha"))#to know the type of value
'''

"""
Arithemetic Operators in python(always binary operaters):can be operated between two operands
1.addition(+)
2.subtraction(-)
3.multiplication(*)
4.division(/)
5.madulas division(%)
5.floor division(//)
6.exponential(**)
"""
#example program(which we given static input)
'''a=10
b=20
print(a+b)
print(a-b)
print(a/b)#division always gives the quotient value in floor type
print(a%b)#result always remainder
print(a*b)
print(a//b)
print(a**b)'''

#Between two strings we can only use +,* operators
#print("poojitha"+"banoth")#add the strings poojithabanoth
#print("poojitha"*2)#multiplies by 2 poojitha+poojitha=poojitha poojithapoojitha


#booleans
#print(true+6)#=>7
#print(false*2)#=>0

#floating points (which produce unpridictable results)
#print(1.0+3.0)
'''
Homework:
Given an 'n' digit integer, find the sum of all the digits in that integer
123=>1+2+3=6
n = input("Enter the number: ")
s = str(n)   
total = 0
for i in s:   
    total = total + int(i)  
print( total)
'''
s="hello"
for i in s:
    print(i)


#print(true+3) coverts type into int convertion
#explicit conversion(int(),float())
#print(int(5.4))#5
#print(float(5))#5.0
#print(int("5.4"))# we can't directly convert it into integer first we have to convert it into float then we convert it into integer

#"",0,0.0=>all are false values other than this arw the true

#taking input from the user (dynamic type)
#python always consider the inputs as the string
'''num=input("enter a number")
print(num,type(num))
num=int(num)#it becames integer
print(num,type(num))'''
