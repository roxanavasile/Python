phone_number = input('Enter phone number: ')

# phone_number.method(argument) --> the general format

phone_number = phone_number.strip()


phone_number = phone_number.replace('(','')


phone_number = phone_number.replace(')','')


phone_number = phone_number.replace('-','')
print("Phone number with extra characters tripped: ",phone_number)
