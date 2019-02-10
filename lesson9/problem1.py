def main():
    dollar_amount=float(input('Please enter the US dollar amount:'))
    conversion_rate=float(input('Please enter the convesion rate:'))
    convert_to_yen(dollar_amount,conversion_rate)

def convert_to_yen(dollar_amount,conversion_rate):
    yen=dollar_amount*conversion_rate
    print('Equivalent amount in Japanese Yen:', yen)


main()
