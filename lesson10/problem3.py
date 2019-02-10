def main():
    number_one,number_two=get_numbers()
    large,small=large_small(number_one,number_two)
    print('The larger number is:', large)
    print('The smaller number is:', small)

def get_numbers():
    number_one=float(input('Enter a number:'))
    number_two=float(input('Enter another number:'))
    return number_one,number_two

def large_small(number_one,number_two):
    if number_one > number_two:
        return number_one, number_two
    else:
        return number_two,number_one

main()


