gallons_of_water=float(input("Enter gallons of water used:"))
if gallons_of_water <= 8000:
    water_bill= gallons_of_water*0.004
    print("Your water bill is: " , water_bill )
else:
    excess_consumption=gallons_of_water-8000
    excess_consumption_price=excess_consumption*0.007
    primary_consumption=8000
    primary_consumption_price=primary_consumption*0.004
    final_price=excess_consumption_price+primary_consumption_price

    print("Your water bill is: $",final_price )
