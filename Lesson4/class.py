print('Welcome to the voice mail system of the college transfer division.')
print('Please enter 1 for English department')
print('Please enter 2 for Math department')
print('Please enter 3 for Physics department')
print('Please enter anything else to reach the secretary.')
deptChoice = input('Enter department choice: ')

if deptChoice == '1':
    print('You have reached the English department.')
    print('Please enter 1 for Richard Cox')
    print('Please enter 2 for James Miffin')
    print('Please enter anything else to reach the secretary.')
    instChoice = input('Enter instructor choice: ')
    if instChoice == '1':
        print('You have reached the voice mail of Richard Cox.')
    elif instChoice == '2':
        print('You have reached the voice mail of James Miffin.')
    else:
        print('You have reached the secretary of the division.')
elif deptChoice == '2':
    print('You have reached the Math department.')
elif deptChoice == '3':
    print('You have reached the Physics department.')
else:
    print('You have reached the secretary of the division.')
