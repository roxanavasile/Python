def main():
    question1() #there is a print in the example, why?
    question2()

def question1():
    print('Question 1:')
    print('The physical devices that a computer is made of are referred to as _ .')
    print('a. hardware')
    print('b. software')
    print('c. the operation system')
    print('d. tools')
    answer=input('Please enter your answer:')
    if answer == 'a':
        print('Correct.')
    elif answer == 'b':
        print('Incorect.')
    elif answer == 'c':
        print('Incorect.' )
    elif answer == 'd':
        print('Incorect.' )

def question2():
    print('Question 2:')
    print('The part of a computer that runs programs is called _ .')
    print('a. RAM')
    print('b. secondary storage')
    print('c. main memory')
    print('d. the CPU ')
    answer2=input('Please enter your answer:')
    if answer2 == 'a':
        print('Incorect.')
    elif answer2 == 'b':
        print('Incorect.')
    elif answer2 == 'c':
        print('Incorect.' )
    elif answer2 == 'd':
        print('Corect.' )

main()
