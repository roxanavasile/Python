
def main():
    print('Enter 1 to calculate BMI only.')
    print('Enter 2 to calculate high blood presure.')
    print('Enter 3 to calculate both')
    choice=int(input('Please enter your choice:'))
    if choice == 1:
        bmi()
    elif choice == 2:
        hypertension()
    elif choice == 3:
        bmi()
        hypertension()



def bmi():
    height=float(input('Please enter your height:'))
    weight=float(input('Please enter your weight:'))
    calc_bmi=(703*weight)/(height*height)
    print('Your BMI is:',calc_bmi)

def hypertension():
    systolicPressure=float(input('Please enter  your systolic pressure:'))
    diastolicPresure=float(input('Please enter your diastolic presure:'))
    if systolicPressure >= 140 or diastolicPresure >=90 :
        print('You have high blood presure.')
    else:
        print('You do not have high blood presure.')



main()






