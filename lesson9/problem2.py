def main():
    age=float(input('Please enter your age:'))
    restHeartRate=float(input('Please enter your resting heart rate:'))
    heart_rate_calculator(age,restHeartRate)


def heart_rate_calculator(age,restHeartRate):
    targetHeartRate=(220-age-restHeartRate)*0.4+restHeartRate
    print('Your target heart rate is:', targetHeartRate)

main()
