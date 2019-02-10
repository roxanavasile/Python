import random
list1=[]
for count in range(30):
    numbers=random.randint(1,4)
    list1.append(numbers)
print(list1)


total=0.0
list2=[]
list2=list1[0:15]
for value in list2:
    total += value

average=total/len(list2)
print('the average of the first 15 elements is:', average)

total=0.0
list3=[]
list3=list1[15:30]
for value in list3:
    total += value

average2=total/len(list3)
print('The average of the last 15 elements is :',average2)

