admission_fee= 20
age=float(input('Enter your age: '))
military_forces="yes"or"no"
military_forces=input("Please confirm military status: ")
if age<12 or military_forces=="yes":
    admission_fee=10
    print("Please pay $10")

else:
    print("Please pay $20")


