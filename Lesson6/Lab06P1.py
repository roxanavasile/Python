keep_going = 'Y'
while keep_going == 'Y':
    salary = float(input('Enter current salary: '))
    newSalary = salary * 1.04
    print('Your new salary is $', newSalary)
    keep_going=input('Do you want to calculate another salary? (Enter Y for yes):')
    keep_going=keep_going.upper()


