#walrus operater:it allows you to assign a value to variable as part of expression(:=)
'''if(x:=len("hello"))>3:
    print(x)'''

#another way comparing with walrus operater
'''s=input() 
x=len(s)
if x>3:
    print(x)'''

#itterations(loops)
#for loor(for variable in sequence )
"""variable is like counter,sequence is like condition"""
'''for i in [1,2,3,4,5]:
    print(i)'''
   #range:we have to give start range and end range(used to replace the sequence)
'''for i in range(1,101):
    print(i,end=" ") '''
#to itterate in reverse order we use (start,stop,step:used to define how much you to increment or decrement)
'''print(range(1,10,2))#step example prints 1 3 5 7 9'''
''''for i in range(101,1,-1):
    print(i)'''

#while(use when we dont know no of condition)
'''while(condition):repeats until condition is true'''
'''counter=0
while counter<10:
    print("pooj",end=" ")
    print(counter,end=" ")
    counter=counter+1'''
#for i in range(1,11):
    #print("5 X",i,"=",i*5)
"""5X 1 = 5
5X 2 = 10
5X 3 = 15
5X 4 = 20
5X 5 = 25
5X 6 = 30
5X 7 = 35
5X 8 = 40
5X 9 = 45
5X 10 = 50"""
#continue(skip the itteration),break(terminates the loop)
# for i in range(1,10):
#     if(i==6):
#         continue
#     print(i)
#while
i=0
while i<10:
    if i==6:
        continue
    print(i)
    i=i+1


# for i in range(1,10):
#     if(i==6):
#         break
#     print(i)









































































































































































































































































































































