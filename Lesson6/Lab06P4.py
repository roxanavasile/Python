speed = float(input('What is the speed miles/hour?'))
hours = int(input('How many hours has the vehicle traveled for?'))

#print the table headings
print('Hour\tDistance')
print('----------------')
for num in range(1,hours+1):
    distance=num*speed
    print(num, distance)
