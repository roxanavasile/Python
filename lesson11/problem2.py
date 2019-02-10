import random

list1=[]
for count in range(10):
    numbers=random.randint(1,4)
    list1.append(numbers)
    print(list1)


list2=list1[5:11]
print("\n")
print(list2)

list2.remove(2)
print("\n")
print(list2)


