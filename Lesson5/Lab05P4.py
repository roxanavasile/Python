_author_='Roxana Vasile'
#This program calculates the water bill

customer=input('Enter R for residential customer and B for business customer:')
water=float(input('Enter the number of gallons used:'))
customer=customer.upper()
if customer=='R':
    if water<=8000:
        cost=water*0.004
        print('Your water bill is ', cost)
    else:
        excess_water=water-8000
        cost_excess=excess_water*0.007
        water=0.004*8000
        total_cost=water+cost_excess
        print('Your water bill is:',total_cost)
elif customer=='B':
    if water<=10000:
        cost=water*0.005
        print('Your water bill is:', cost)
    else:
        excess_water=water-10000
        cost_excess=excess_water*0.009
        water=10000*0.005
        total_cost=water+cost_excess
        print('Your water bill is:',total_cost)

