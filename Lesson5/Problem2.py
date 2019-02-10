_author_='Roxana Vasile'

software=int(input("How many copies are you buying? Enter:"))

if software >=1 and software <= 10:
    unit_price=99
    total_price=99*software
    print('Unit price is $99.')
    print('Your total price is $',total_price)

elif software >=11 and software<=50:
    unit_price=89
    total_price=unit_price*software
    print('Unit price is $89.')
    print('Your total price is $', total_price)

elif software >=51 and software <= 100:
    unit_price=79
    total_price=unit_price*software
    print('Unit price is $79.')
    print('Your total price is $',total_price)

elif software>=101:
    unit_price=69
    total_price=unit_price*software
    print('Unit price is $69.')
    print('Your total price is $', total_price)
