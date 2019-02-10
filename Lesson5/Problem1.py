_author_='Roxana Vasile'

print("Please enter a health plan by entering the health plan code.")
print("Please enter E for employee only")
print("Please enter S for employee and spouse")
print("Please enter C for employee and children")
print("Please enter F for the whole family")

health_plan=input('Health plan choice: ')
health_plan=health_plan.upper()
if health_plan == 'E':
    print('The premium is $40.')
elif health_plan == 'S':
    print('The premium is $160.')
elif health_plan == 'C':
    print('The premium is $200')
elif health_plan == 'F':
    print('The premium is $250.')
else:
    print('Invalid health plan code.')
