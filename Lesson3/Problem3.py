original_price=float(input("Enter original price: "))
decimal_dicount=float(input("Enter decimal discount: "))
sale_discount=original_price*decimal_dicount
sale_price=original_price-sale_discount
sale_tax=sale_price*0.07
amount_due=sale_price+sale_tax
print("Display sales price:",sale_price)
print("Display sales tax:", sale_tax)
print("Display amount due:", amount_due)
