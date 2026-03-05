# nums=list(map(int,input().split()))
# print(nums)

# # example to use the i as index
# scores=[10,20,30,40,50]
# for i in range(len(scores)):
#     print(i, scores[i])
# #example where i as an value
# for i in scores:
#     print(i)


# 
numbers = list(map(int, input().split()))

maximum = numbers[0]

for num in numbers:
    if num > maximum:
        maximum = num

print("Maximum value:", maximum)
print("Position:", numbers.index(maximum))
