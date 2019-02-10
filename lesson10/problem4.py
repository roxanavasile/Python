import length


def main():
    inches=float(input('How many inches?'))
    cm=length.inches_to_cm(inches)
    print('It is equivalent to', cm, 'cm')
    feet=float(input('How many feet?'))
    m=length.feet_to_m(feet)
    print('It is equivalent to',m,'m')
    miles=float(input('How many miles?'))
    km=length.miles_to_km(miles)
    print('It is equivalent to', km, 'km')

main()




