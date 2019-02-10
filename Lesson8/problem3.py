def main():
    distance_in_kilometers=float(input('Please enter the distance in kilometers:'))
    convert_to_miles(distance_in_kilometers)



def convert_to_miles(distance_in_kilometers):
    miles=distance_in_kilometers*0.6214
    print('It is equivalent to:', miles)

main()
