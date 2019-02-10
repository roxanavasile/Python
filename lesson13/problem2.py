#a
product=input('Enter the 4-digit product code: ')

#b
product=product.strip() # strips all leading and trailing whitespace characters from the code



#c
if not product.isdigit(): #if product is not all digits
    print('Product code must consist of digits only.')


#d

elif not len(product) == 4:
    print('Product code must contain  exactly 4 digits.')


#e
elif product.endswith('4'):
    print('This orange is from California.')
else:
    if product.endswith('7'):
     print('This orange is from Florida.')
    else:
     print('the last digit must be 4 or 7.')

