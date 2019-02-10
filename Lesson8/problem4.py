def main():
    in_or_out=input('Are you in state student? [y/n]')
    credit_hours=int(input('How many credit hours are you taking?'))

    if in_or_out == 'y':
        print('You are paying in-state tuition.')
        tuition_instate(credit_hours)

    elif in_or_out == 'n':
        print('You pay out of state tuition.')
        tuition_outstate(credit_hours)

def tuition_instate(credit_hours):
    if credit_hours <= 12:
        tuition=60*credit_hours
    else:
        tuition=60*12
    print('Please pay:', tuition)

def tuition_outstate(credit_hours):
    if credit_hours <=15:
        tuition=200*credit_hours
    else:
        tuition=200*15
    print('Please pay:', tuition)


main()
