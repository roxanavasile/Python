disc_purchased=int(input("Enter the number of discs purchased or -1 to stop:"))
while disc_purchased != -1:
    total= disc_purchased*4.99 + 2.99
    print("Please pay this amount",total)
    disc_purchased=int(input("Enter the number of discs purchased or -1 to stop:"))
