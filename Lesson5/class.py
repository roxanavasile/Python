sales = float(input('Enter the amount of sales: '))
comm_rate = float(input('Enter the commission rate: '))
commission = sales * comm_rate
print('The commission is $', commission)
keep_going = input('Do you want to calculate another commission (Enter y for yes): ')
keep_going = keep_going.lower()
while keep_going == 'y':
    sales = float(input('Enter the amount of sales: '))
    comm_rate = float(input('Enter the commission rate: '))
    commission = sales * comm_rate
    print('The commission is $', commission)
    keep_going = input('Do you want to calculate another commission (Enter y for yes): ')
    keep_going = keep_going.lower()
