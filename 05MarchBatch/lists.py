#lists
#looping list


#sclicing
#->to extract the portion of list it can be possible using slicing
abc=[4,1,9,2,7]
'''print(abc[-2:-4:-1])
print(abc[-4:-2:-1])
print(abc[-2:-4:1])'''

#to rverse the list
'''for i in range(len(abc)-1,-1,-1):
     print(abc[i])'''

#len
# append(add element at the end)
#extend:
#insert(index,element):to insert the element at middle of list
#remove(element):to remove elent(all ways remove first appearence) 
#pop(index):to remove element using the index

#Functions:a block of code
'''def square(n):
    ans=n*n
    print(ans)
square(10)


#return used to say answer to function
def square(n):
    ans=n*n
    ans2=n*n*n
    return ans
x=square(10)
print(x)


def square(n):
    ans=n*n
    return ans
x=square(10)
print(x)'''


def isMoreThan(n):
    if n>100:
        return True
    return False
ans=isMoreThan(42)
print(ans)

def printName(name):
    print(name)
    return
ans=printName("tanishq")
print(ans)






