#Assignment/
'''#enter the how many items you want 
#use loop to take the price of the each item
#calculates the total bill
n=int(input("how many items we need "))
total_bill=0
for i in range(0,n):
    price=int(input(f"Enter the price {i}:"))
    total_bill=total_bill+price
    print(f"item is {i}, nd price:{price}")
print(f"total bill is :{total_bill}")'''


product_names:[]
product_price:[]
def add_product(name,price):
    product_names.append(name)
    product_price.append(price)

def total_value():
    for i in product_price:
        total+=i

def find_most_expensive():
    maxExpence=product_price[0]
    maxExpenceItem=product_price[0]

    for i in range(1,product_price):
        if product_price[i]>maxExpence:
            maxExpence=product_price[i]
            maxExpenceItem=product_names[i]
    return maxExpence,maxExpenceItem

        






