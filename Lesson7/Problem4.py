total = 0
number=int(input("Enter the number of donors today:"))
for i in range(number):
    donation=float(input("Enter the amount of donation:"))
    while donation <= 0:
        print('The donation cannot be negarive.')
        donation=float(input("Enter the amount of donation:"))
    total = donation + total
print('Total money raised today: ', total)
