""" *** STRINGS *** """
#->we can perform same index as list 
#->strings are immutable we cant 
#->concatination (+)
      #name=Tanish to change charecters name=name[0:3]+"p"+name[4:]
#.upper()=>chane into upper case
#.lower()=>change string to lower

#=> name="tanishq" to check whether ishq is present in name we use in operater
# ==> in operater to check the group of charecters present in string or not and it returns the true or false as output



'''**** Dictionary ***'''
#->stores data in the form of key-value pair
#-> we always search values in dictionary using the keys
#->keys should always be immutable
'''Tanishq={name:"tanishq",age:20,native:"colcutta"}'''
#->to acess the value in above dictionary print(Tanishq["name"])
#to print all keys Tanishq.keys()
'''tanishq_information={
    "name":"tanishq",
    "age":20,
    "native":"colcutta",
    "surname":"Guptha",
    "subjects":["Telugu","Hindi","English"]
    }
print(tanishq_information.keys())
print(tanishq_information("subjects"))'''

#nested dictionary
tanishq_information={
    "name":"tanishq",
    "age":20,
    "native":"colcutta",
    "surname":"Guptha",
    "subjects":["Telugu","Hindi","English"],
    "address":{ "name":"tanish",
               "city":"Delhi"           

    }
    #when i access the key which is not in dictionary it throws error but i dont need that so we use
    }

print(tanishq_information["address"]["city"])#Delhi
#when i access the key which is not in dictionary it throws error but i dont need that so we use
print(tanishq_information.get("hi"))#returs none

# to add new pair in key
tanishq_information["habbit"]="Reading"
#to acess all the keys 
tanishq_information.keys()
#to acess all the values 
tanishq_information.values()
print(tanishq_information["address"].values())
print(tanishq_information["address"].keys())
#to get entir dictionary
print(tanishq_information.items())

#to delete the key
del tanishq_information["name"]#deletes the name key
tanishq_information.pop("name")
#to delete the last entry
tanishq_information.popitem()

#to get the lenth of the dictionary
print(len(tanishq_information.items()))

#to combine the two dictionaries for that we use .update method
d1={"a":1,"b":2}
d2={"c":3,"d":4}
d1.update(d2)#priority is given to the last declared values


#itteration on dictionary
user_info={
    "name":"tanishq",
    "surname":"guptha",
    "class":10,
    "age":54,
    "native":"Agra"

}
#to itteraye on the keys
for key in user_info.keys():
    print(key,user_info[key])
#to itteraye on the values
for value in user_info.values():
    print(key,user_info[value])8
#another way
for key in user_info:
    print(key)
#to return pair
for key,value in user_info.items():
    print(f"keys is {key} and the value {value}")


