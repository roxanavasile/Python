keep_going='Y'
while keep_going=='Y':
    college = input('Enter name of college:')
    tuition = float(input('Enter the tuition amount:'))
    room = float(input('Enter the room amount:'))
    board = float(input('Enter the board amount:'))
    other_expenses = float(input('Enter the other expenses amount:'))
    financial_aid = float(input('Enter the financial aid amount:'))
    total_cost = tuition + room + board + other_expenses - financial_aid
    print( 'Your out-of-pocket cost will be:', total_cost)
    keep_going = input('Do you want to calculate the cost for another college? (Enter Y for yes)')
    keep_going = keep_going.upper()
