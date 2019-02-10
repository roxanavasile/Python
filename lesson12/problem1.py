import random

list1=[]

for count in range(10):
    numbers=random.randint(1,4)
    list1.append(numbers)
print(list1)
print('\n')

list2=[]
list2=[]+list1
print(list2)
print('\n')

list3=[]
for item in list1:
    list3.append(item)
print(list3)
print('\n')

list4=[]
list4=list1[:]
print(list4)
