def main():

    total= choose_sandwich()+choose_side()+choose_drink()
    print('Please pay this amount:', total)

def choose_sandwich():
    print('Pick a sandwich:')
    print('1.grilled cheese sandwich : $3.00')
    print('2.chicken sandwich: $3.50')
    print('3.turkey sandwich: $4.00')
    sandwich=int(input('Please enter your choice:'))
    if sandwich == 1:
        cost = 3
        return cost
    elif sandwich == 2:
        cost = 3.50
        return cost
    elif sandwich == 3:
        cost = 4
        return cost

def choose_side():
    print('Pick a side:')
    print('1.french fries: $1.50')
    print('2.mashed potatoes: $1.50')
    print('3.green beans: $1.25')
    print('4.garden salad: $2.00')
    side=int(input('Please enter your choice:'))
    if side == 1:
        cost = 1.50
        return cost
    elif side == 2:
        cost = 1.50
        return cost
    elif side == 3:
        cost = 1.25
        return cost
    elif side == 3:
        cost = 2
        return cost

def choose_drink():
    print('Pick a drink:')
    print('1.Coffee: $1.25')
    print('2.Iced Tea: $1.00')
    print('3.soda: $1.00')
    side=int(input('Please enter your choice:'))
    if side == 1:
        cost= 1.25
        return cost
    elif side == 2:
        cost = 1
        return cost
    elif side == 3:
        cost = 1
        return cost
main()


